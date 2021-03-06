#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from marshmallow import Schema, fields, post_load
from sqlalchemy import Integer, String, Column

from light_blog.model import db
from light_blog.model.post_tag import post_tag
from light_blog.model.user_role import user_role


class Role(db.Model):
    """标签表，不同文章可以对应不同的标签"""
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    description = Column(String(length=255))

    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Model Role `{}`>".format(self.name)

    def to_json(self):
        schema = RoleSchema(strict=True)
        return schema.dump(self).data


class RoleSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String()

    @post_load
    def make_entity(self, data):
        return Role(**data)
