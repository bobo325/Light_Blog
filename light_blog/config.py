#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""


class Config(object):
    """Base config class."""
    SECRET_KEY = 'imissyou.online'


class ProdConfig(Config):
    """Production config class."""
    pass


class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:chenbo@localhost:3306/light_blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# import os
#
# """
# 环境开关   prod  test  local
# """
# config = str(os.environ.get("CONFIG", 'dev')).strip()
#
#
# if config == "prod":
#     from config.prod import *
# elif config == "test":
#     from config.test import *
# else:
#     from config.dev import *