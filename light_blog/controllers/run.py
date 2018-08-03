#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from flask import Flask, redirect, url_for

import os

from light_blog.extensions import bcrypt
from light_blog.route import blog_blueprint
from light_blog.model import db


def create_app(object_name):
    basedir = os.path.dirname(__file__)

    static_path = os.path.abspath(os.path.join( basedir,  os.path.pardir, 'static'))

    app = Flask(__name__, static_url_path='/static', static_folder=static_path)

    app.config.from_object(object_name)

    # views = __import__('light_blog.route.blog')  #有了蓝本注册之后就不需要import了

    # sqlalchemy绑定app
    db.init_app(app)
    bcrypt.init_app(app)  # bcrypt 也是通过在app注册的

    # 重定向至首页目录
    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blueprint=blog_blueprint)
    return app
