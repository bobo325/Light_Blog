#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from flask import Flask, redirect, url_for

from light_blog.config import DevConfig, Config
import os

from light_blog.route import blog_blueprint
from light_blog.model import db

basedir = os.path.dirname(__file__)
# import pdb
# pdb.set_trace()
static_path = os.path.abspath(os.path.join( basedir,  os.path.pardir, 'static'))

app = Flask(__name__, static_url_path='/static', static_folder=static_path)
# print(static_path)
# print(__name__)
# print(__file__)


app.config.from_object(DevConfig)
app.config.from_object(Config)
# print(app.config.get('SQLALCHEMY_DATABASE_URI'))  # 说明已经获取到地址了
views = __import__('light_blog.route.blog')
# Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
db.init_app(app)


# 重定向至首页目录
@app.route('/')
def index():
    return redirect(url_for('blog.home'))


app.register_blueprint(blueprint=blog_blueprint)
if __name__ == '__main__':
    app.run()
