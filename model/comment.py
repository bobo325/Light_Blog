#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from model import db


class Comment(db.Model):
    """每一篇文章都对应很多评论（1：n）"""

    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    text = Column(Text)
    date = Column(DateTime, default=datetime.now())
    post_id = db.Column(db.String(45), db.ForeignKey('post.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.name)