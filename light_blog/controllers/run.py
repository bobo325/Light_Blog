#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from flask import Flask

from light_blog.config import DevConfig, Config
import os
basedir = os.path.dirname(__file__)
# import pdb
# pdb.set_trace()
static_path = os.path.abspath(os.path.join( basedir,  os.path.pardir, 'static'))

app = Flask(__name__, static_url_path='/static', static_folder=static_path)
# print(static_path)
# print(__name__)
# print(__file__)

# from model import db
# Inport the vies module
# from views import *

app.config.from_object(DevConfig)
app.config.from_object(Config)
# print(app.config.get('SQLALCHEMY_DATABASE_URI'))  # 说明已经获取到地址了
views = __import__('light_blog.route.blog')

if __name__ == '__main__':
    app.run()
