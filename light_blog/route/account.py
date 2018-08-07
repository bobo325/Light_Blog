# !/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""

from flask import url_for, flash, render_template, request, session, current_app
from flask_login import logout_user
from flask_principal import identity_changed, AnonymousIdentity
from werkzeug.utils import redirect

from light_blog.extensions import qq
from light_blog.forms import LoginForm, RegisterForm
from light_blog.model import db
from light_blog.model.user import User
from light_blog.route import account_blueprint

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""


# @account_blueprint.route('/')     # 默认只支持GET方法
# def index():
#     return redirect(url_for('blog.home'))


@account_blueprint.route('logout', methods=['GET', 'POST'])
def logout():
    """View function for logout."""
    logout_user()    # 将用户从session中删除

    # identity_changed.send(
    #     current_app._get_current_object(),
    #     identity=AnonymousIdentity())  # 将用户身份变为匿名身份

    flash("You have been logged out.", category="success")
    return redirect(url_for('account.login'))


@ account_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """View function for Register."""

    # Will be check the username whether exist
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Your user has been created, please login.', category="success")
        return redirect(url_for('account.login'))
    flash('Your user created failed, please try again.', category="error")
    return render_template('register.html',
                           form=form)


# 当访问/facebook时，出发授权流程
@account_blueprint.route('/facebook')
def facebook_login():
    return qq.authorize(
        callback=url_for('account.facebook_authorized',
                         next=request.referrer or None,
                         _external=True))


# 该视图接受从facebook认证服务器返回的resp对象
@account_blueprint.route('/facebook_authorized')   # 修改应用域名到线上环境 配置Facebook配置
@qq.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description'])

    session['facebook_oauth_token'] = (resp['access_token'], '')

    me = qq.get('/me')

    if me.data.get('first_name', False):
        qq_username = me.data['first_name'] + " " + me.data['last_name']
    else:
        qq_username = me.data['name']

    user = User.query.filter_by(username=qq_username).first()
    if user is None:
        user = User(username=qq_username, password='chenbo')
        db.session.add(user)
        db.session.commit()

    flash('You have been logged in.', category='success')

    return redirect(url_for('blog.home'))