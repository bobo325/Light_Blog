#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""


class Config(object):
    """Base config class."""
    SECRET_KEY = 'imissyou.online'

    # reCAPTCHA Public key and Private key
    RECAPTCHA_PUBLIC_KEY = "6LcWCmgUAAAAAJ65XRBGvV3hOEjgrOJMloq7c8HO"
    RECAPTCHA_PRIVATE_KEY = "6LcWCmgUAAAAADiamtF6IyUe_GEL4hDYaND3xpoo"


class ProdConfig(Config):
    """Production config class."""
    pass


class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:chenbo@light_blog_mysql:3306/light_blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery < -- > RabbitMQ connection
    CELERY_RESULT_BACKEND =  "amqp://chenbo:chenbo@rabbitmq:5672//"    # TODO 上线得重新设置
    CELERY_BROKER_URL = "amqp://chenbo:chenbo@rabbitmq:5672//"


ACCOUNT = "1126531273@qq.com"
PASSWORD = "lbaucstdiigjjefc"  # 第三方客户登陆密码
EMAIL_CONTEXT = "终于等到您！欢迎来到博客的全新世界!"

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
