#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from flask import Flask

from config import DevConfig

app = Flask(__name__)

app.config.from_object(DevConfig)


@app.route('/')
def hello_world():
    return '<h1>Welcome To My Project!</h1>'


if __name__ == '__main__':
    app.run()
