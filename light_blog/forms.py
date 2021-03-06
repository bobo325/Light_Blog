#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
  # 更具有安全性
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo

from light_blog.model.user import User


class CommentForm(FlaskForm):
    """Form validator for comment."""

    # Set some field(InputBox) for enter the data.
    # patam validators: setup list of validators
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)])
    text = StringField(u'Comment', validators=[DataRequired()]) # Text deprecated


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField('Remember Me')  # “记住我”的功能很难实现。但是，Flask-Login 几乎透明地实现它
    #  - 只要把 remember=True 传递给 login_user。一个 cookie 将会存储在用户计算机中

    def validate(self):
        """Validator for check the account information."""
        check_validate = super(LoginForm, self).validate()
        if not check_validate:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid UserName.')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid Password.')
            return False
        return True


class RegisterForm(FlaskForm):
    """Register Form"""
    username = StringField('Username', [DataRequired(), Length(max=255)])
    email = EmailField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    comfirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    # recaptcha = RecaptchaField()  # TODO 正式环境还要修改应用域名

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        # If validator no pass
        if not check_validate:
            return False

        # Check the user whether already exist.
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append('User with the name already exists.')
            return False
        return True


class PostForm(FlaskForm):
    """Post Form"""
    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Blog Content', [DataRequired()])
