# !/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from datetime import datetime

from marshmallow import Schema, fields, post_load
from sqlalchemy import DateTime, Column, String, Text, Integer, Boolean

from light_blog.model import db
from light_blog.model.post_tag import post_tag


class Post(db.Model):
    """用来表示Blog中的文章"""
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = db.Column(String(255))
    text = Column(Text)
    publish_date = Column(DateTime, default=datetime.now())
    # Set the foreign key for Post
    user_id = Column(Integer, db.ForeignKey('user.id'))  # 外键foreignKey
    is_delete = Column(Boolean, default=False)
    # 如果没指定__tablename__属性，那么上一句:ForeignKey('User.id'),即和py文件对应
    comment = db.relationship(
        'Comment',
        backref='post',  # 声明表的关系是双向的
        lazy='dynamic'   # 决定了什么时候从数据库中加载数据：select, joined, subquery, dynamic
    )
    tag = db.relationship(
        'Tag',
        secondary=post_tag,  # 告知sqlalchemy该many_to_many的关联保存在post_tag中
        backref=db.backref('post', lazy='dynamic')
    )

    def __init__(self, title, text, publish_date, user_id):
        self.title = title
        self.text = text
        self.publish_date = publish_date
        self.user_id = user_id
        self.is_delete = False

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)

    def to_json(self):
        schema = PostSchema(strict=True)
        return schema.dump(self).data


class PostSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String()  # default='chenbo'
    text = fields.String()  # default='chenbo'
    publish_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    user_id = fields.Integer()
    is_delete = fields.Boolean()

    @post_load
    def make_entity(self, data):
        return Post(**data)