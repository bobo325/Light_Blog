#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from sqlalchemy import Integer

from model import db

#
# class PostTag(db.Model):
#     """文章和标签关联表 多对多"""
#     __tablename__ = "post_tag"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     post_id = Column(Integer, db.ForeignKey('post.id'))
#     tag_id = Column(Integer, db.ForeignKey('tag.id'))


post_tag = db.Table('post_tag',
    db.Column('id', Integer, primary_key=True, autoincrement=True),
    db.Column('post_id', Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', Integer, db.ForeignKey('tag.id')))
