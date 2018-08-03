#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""

import datetime

from flask import render_template, url_for, redirect
from sqlalchemy import func

from light_blog.forms import CommentForm, PostForm
from light_blog.model import db


from light_blog.model.post_tag import post_tag
from light_blog.model.comment import Comment
from light_blog.model.post import Post
from light_blog.model.tag import Tag

# NOTE 1: 由于每个页面都需要右侧边栏的数据, 所以将这些高重用的代码抽象成为一个函数.
# NOTE 2: sidebar_data() 函数中调用了 sqlalchemy.func 库, func 库提供了一个计数器 count,
#         用于返回 tags 表中值相同的 post_id 列的数量，来得到 post 数最多的 tags。
# NOTE 3: 因为 views.py 会作为所有视图函数的定义文件, 所以将 main.py 中的视图函数 home() 迁移到该文件中.
from light_blog.model.user import User
from light_blog.route import blog_blueprint


# @app.route('/test')
def sidebar_data():
    """Set the sidebar function."""

    # get post of recent
    recent = Post.query.order_by(Post.publish_date.desc()).\
        limit(5).all()

    # get tags and sort by count of posts.
    top_tags = db.session.query(Tag, func.count(post_tag.c.post_id).label('total')).\
        join(post_tag).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags


# @blog_blueprint.route('/')
# def hello_world():
#     top_tags = db.session.query(Tag, func.count(post_tag.c.post_id).label('total')). \
#         join(post_tag).group_by(Tag).order_by('total DESC').limit(5).all()
#     for one in top_tags:
#         print(top_tags)
#         print(one)
#         print(one[0])
#     return render_template("index.html")


# 查询文章列表
@blog_blueprint.route('/')      # app.route() 函数中可以定义多样的 URL 路由规则, 也可以为一个视图函数定义多条 URL 路由规则,
                                # 在这个 Blog 项目中的 URL 设计应该遵循 RESLful 风格
@blog_blueprint.route('/<int:page>')
def home(page=1):
    """View function for home page"""

    post = Post.query.order_by(
        Post.publish_date.desc()
    ).paginate(page, 10)
    recent, top_tags = sidebar_data()
    return render_template('home.html',  # flask提供的render_template()函数，就是将
                           # 视图函数和Jinja模板文件关联起来的桥梁
                           post=post,  # 文章内容
                           recent=recent,  # 最近五篇文章
                           top_tags=top_tags)  # 数量最多的五个标签


# 查询某一篇文章
# 路由方法route()默认只接受POST请求；form.validata_on_submit()
# 方法会隐式的判断该 HTTP 请求是不是 POST, 若是, 则将请求中提交的表单数据对象传入上述的 form 对象并进行数据检验.
@blog_blueprint.route('/post/<int:post_id>', methods=('GET', 'POST'))
def post(post_id):
    """View function for post page"""
    # 先做验证
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(name=form.name.data,
                              text=form.name.data,
                              date=datetime.datetime.now(),
                              post_id=post_id)
        db.session.add(new_comment)
    post = db.session.query(Post).get_or_404(post_id)
    tags = post.tag  # 关联外键 一对多查询简化
    comments = post.comment.order_by(Comment.date.desc()).all()
    recent, top_tags = sidebar_data()
    db.session.commit()
    return render_template('post.html',
                           post=post,
                           tags=tags,
                           comments=comments,
                           form=form,
                           recent=recent,
                           top_tags=top_tags)


# @blog_blueprint.route('/tag/<string:tag_name>')
def tag(tag_name):
    """View function for tag page"""

    tag = db.session.query(Tag).filter_by(name=tag_name).first_or_404()
    posts = tag.post.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('../light_blog/templates/blog/tag.html',
                           tag=tag,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)


# @blog_blueprint.route('/user/<string:username>')
def user(username):
    """View function for user page"""
    user = db.session.query(User).filter_by(username=username).first_or_404()
    posts = user.post.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('../light_blog/templates/blog/user.html',
                           user=user,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)


@blog_blueprint.route('/new', methods=['GET', 'POST'])
def new_post():
    """View function for new_port"""
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data,
                        text=form.text.data,
                        publish_date=datetime.now(),
                        user_id=1)                      # TODO 后需修改
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.home'))

    return render_template('new_post.html',
                           form=form)


@blog_blueprint.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit_post(id):
    """View function for edit_post."""

    post = Post.query.get_or_404(id)
    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        post.publish_date = datetime.datetime.now()

        # Update the post
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.post', post_id=post.id))

    form.title.data = post.title
    form.text.data = post.text
    return render_template('edit_post.html', form=form, post=post)

