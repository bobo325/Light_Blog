#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: Chenbo
@contact: 1126531273@qq.com
@time: 2018/05/15 14:05
"""

db_config = {
    "url": "mysql://root:chenbo@localhost:3306/blog"
    # "url": "mysql+mysqldb://root:chenbo@localhost/blog"
}

web_config = {
    "ip": "0.0.0.0",
    "port": 8888,
    "debug": True,
    "upload_file_max_size": 8 * 1024 * 1024,
    "session_expire_time": 180 * 24 * 3600
}