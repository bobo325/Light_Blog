#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from sqlalchemy import Integer

from light_blog.model import db

#
# class PostTag(db.Model):
#     """文章和标签关联表 多对多"""
#     __tablename__ = "post_tag"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     post_id = Column(Integer, db.ForeignKey('post.id'))
#     tag_id = Column(Integer, db.ForeignKey('tag.id'))


user_role = db.Table('user_role',
    db.Column('id', Integer, primary_key=True, autoincrement=True),
    db.Column('user_id', Integer, db.ForeignKey('user.id')),
    db.Column('role_id', Integer, db.ForeignKey('role.id'))
                    )
