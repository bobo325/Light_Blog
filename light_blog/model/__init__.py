#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from flask_sqlalchemy import SQLAlchemy

from light_blog.controllers.run import app

db = SQLAlchemy(app)  # 启动sqlalchemy
