#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
import os

from flask import session
from flask_bcrypt import Bcrypt

# Create the Flask-Bcrpyt's instance
from flask_login import LoginManager
from flask_oauth import OAuth


bcrypt = Bcrypt()

# Create the Flask-OAuth's instance
oauth = OAuth()

# facebook 第三方登录接口  # TODO 后期修改facebook应用域名
# Create the auth object for facebook.
facebook = oauth.remote_app(
    'facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key='508576969570241',
    consumer_secret='5fd30b810499a7d752850a1aa11a14ff',
    request_token_params={'scope': 'email'})


@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_oauth_token')


# NOTE 1: facebook 对象是上述步骤中创建的 facebook 应用对象, 其包含了认证的结果
# 信息和请求授权的 facebook user 信息. facebook 是完成第三方登录流程的接口对象.
# NOTE 2: 方法 get_facebook_oauth_token() 获取 facebook 发放的 token.
# 当成功创建 facebook 对象并完成授权时, 表示 client(blog) 成功的向 Authorization server 完成认证并接受到服务端的 token,
# 并保存在 session 中. 然后 Client 就可以使用这个 token 去访问 facebook 的资源(账户权限资源)了.


# Flask-Login
login_manager = LoginManager()

login_manager.login_view = 'account.login'  # 制定登陆页面的视图函数
login_manager.session_protection = 'strong'  # 能够更好的防止恶意用户篡改cookies，当发现cookies被篡改时，用户的session对象会被立即删除，导致强制重新登陆
login_manager.login_message = 'Please login to access this page.'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(user_id):  # 需要定义一个 LoginManager.user_loader 回调函数，它的作用是在用户登录并调用
    # login_user() 的时候, 根据 user_id 找到对应的 user, 如果没有找到，返回None,
    # 此时的 user_id 将会自动从 session 中移除, 若能找到 user ，则 user_id 会被继续保存.
    """Load the user's info."""
    from light_blog.model.user import User
    return User.query.filter_by(id=user_id).first()
