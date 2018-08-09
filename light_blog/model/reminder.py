#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
import datetime

from sqlalchemy import Integer, DateTime, String, Text

from light_blog.model import db


class Reminder(db.Model):
    """Represents Proected reminders."""

    __tablename__ = 'reminder'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    date = db.Column(DateTime(), default=datetime.datetime.now())
    email = db.Column(String(255))
    text = db.Column(Text())

    def __init__(self, email, text):
        self.email = email
        self.data = datetime.datetime.now()
        self.text = text

    def __repr__(self):
        return '<Model Reminder `{}`>'.format(self.text[:20])