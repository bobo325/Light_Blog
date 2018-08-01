#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from flask import Flask
from config import DevConfig, Config

import form   # 导入验证


app = Flask(__name__)
# from model import db
# Inport the vies module
# from views import *

app.config.from_object(DevConfig)
app.config.from_object(Config)
print(app.config.get('SQLALCHEMY_DATABASE_URI'))  # 说明已经获取到地址了
# db = SQLAlchemy(app)

views = __import__('views')
#from views import blog_blueprint

if __name__ == '__main__':
    #app.register_blueprint(blog_blueprint)
    app.run()
