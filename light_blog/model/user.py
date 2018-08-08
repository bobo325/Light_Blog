#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""

from flask_login import AnonymousUserMixin
from flask_login._compat import unicode
from sqlalchemy import Column, String, Integer

from light_blog.extensions import bcrypt
from light_blog.model import db
from marshmallow import Schema, fields, post_load

from light_blog.model.role import Role


class User(db.Model):
    """Represents Proected users"""
    # Set the name for table
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))
    # establish contact with post's foreignkey:user_id
    post = db.relationship(
        'Post',
        backref='user',
        lazy='dynamic'
    )

    def __init__(self, username, password):
        self.username = username
        self.password = self.set_password(password)

        # 每一个新创建的用户都有这个默认角色
        default = Role.query.filter_by(name='default').one()
        self.role.append(default)

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{},{}`>".format(self.username, self.password)

    def set_password(self, password):
        """Convert the password to cryptograph via flask-bcrppt"""
        return bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def to_json(self):
        schema = UserSchema(strict=True)
        return schema.dump(self).data

    def is_authenticated(self):
        """Check the user whether logged in."""
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        """Check the user whether pass the activation process."""

        return True

    def is_anonymous(self):
        """Check the user's login status whether is anonymous."""

        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        """Get the user's uuid from database."""

        return unicode(self.id)


class UserSchema(Schema):
    id = fields.Integer(required=True)
    username = fields.String()  # default='chenbo'
    password = fields.String()  # default='chenbo'

    @post_load
    def make_entity(self, data):
        return User(**data)

# set_password(self, password)：在设定密码的时候，将明文密码转换成为 Bcrypt 类型的哈希值。
# check_password(self, password)：检验输入的密码的哈希值，与存储在数据库中的哈希值是否一致。
