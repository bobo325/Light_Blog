#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from wtforms import StringField, Form, TextField
from wtforms.validators import DataRequired, Length


class CommentForm(Form):
    """Form validator for comment."""

    # Set some field(InputBox) for enter the data.
    # patam validators: setup list of validators
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)])
    text = StringField(u'Comment', validators=[DataRequired()]) # Text deprecated