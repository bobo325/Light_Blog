#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

app = Flask(__name__)
# from model import db
# Inport the vies module
# from views import *

app.config.from_object(DevConfig)
print(app.config.get('SQLALCHEMY_DATABASE_URI'))  # 说明已经获取到地址了
# db = SQLAlchemy(app)

views = __import__('views')

if __name__ == '__main__':
    app.run()
