#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from os import path

from flask import Blueprint

from light_blog.controllers.run import app

blog_blueprint = Blueprint(
    'blog',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'blog'),
    url_prefix='/blog')

# 将关联的路由以子模块的形式导入
from . import blog
app.register_blueprint(blog_blueprint)