#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from sqlalchemy import Column, String, Integer

from model import db
from marshmallow import Schema, fields, post_load


class User(db.Model):
    """Represents Proected users"""
    # Set the name for table
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))

    def __inits__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{},{}`>".format(self.username, self.password)

    def to_json(self):
        schema = UserSchema(strict=True)
        return schema.dump(self).data


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.String()  # default='chenbo'
    password = fields.String()  # default='123456'

    @post_load
    def make_entity(self, data):
        return User(**data)