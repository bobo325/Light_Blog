from datetime import datetime

from marshmallow import Schema, fields, post_load
from sqlalchemy import DateTime, Column, String, Text, Integer

from model import db


class Post(db.Model):
    """用来表示Blog中的文章"""
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = db.Column(String(255))
    text = Column(Text())
    publish_date = Column(DateTime,default=datetime.now())
    # Set the foreign key for Post
    user_id = db.Column(Integer(), db.ForeignKey('user.id'))  # 外键foreignKey
    # 如果没指定__tablename__属性，那么上一句:ForeignKey('User.id'),即和py文件对应
    coments = db.relationship(
        'Comment',
        backref='post',
        lazy='dynamic'
    )

    def __init__(self, title, text, publish_date, user_id):
        self.title = title
        self.text = text
        self.publish_date = publish_date
        self.user_id = user_id

    def __repr__(self):
        return "<Model Post `{}`>".format(self.titles)

    def to_json(self):
        schema = PostSchema(strict=True)
        return schema.dump(self).data


class PostSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String()  # default='chenbo'
    text = fields.String()  # default='chenbo'
    publish_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    user_id = fields.Integer()

    @post_load
    def make_entity(self, data):
        return Post(**data)