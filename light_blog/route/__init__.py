#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from os import path

from flask import Blueprint


blog_blueprint = Blueprint(
    'blog',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'blog'),
    url_prefix='/blog')

account_blueprint = Blueprint(  # 这个路由不设置url_prefix
    'account',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'account'),
    url_prefix='/account'
)
# 将关联的路由以子模块cls的形式导入
from . import blog
from . import account