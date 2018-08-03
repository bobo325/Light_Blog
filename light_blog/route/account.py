# !/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from flask import url_for, flash, render_template
from werkzeug.utils import redirect

from light_blog.forms import LoginForm, RegisterForm
from light_blog.model import db
from light_blog.model.user import User
from light_blog.route import account_blueprint

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""


# @account_blueprint.route('/')     # 默认只支持GET方法
# def index():
#     return redirect(url_for('blog.home'))


@account_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """Veiw function for login."""

    form = LoginForm()
    if form.validate_on_submit():   # return self.is_submitted() and self.validate()
        # 在登录成功之后会返回 [(‘success’, ‘You have been logged in.’)] 的信息
        flash("You have been logged in.", category="success")
        return redirect(url_for('blog.home'))
    return render_template('login.html',
                           form=form)


@account_blueprint.route('logout', methods=['GET', 'POST'])
def logout():
    """View function for logout."""
    flash("You have been logged out.", category="success")
    # return redirect(url_for('blog.home'))
    return render_template('login.html')


@ account_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """View function for Register."""

    # Will be check the username whether exist
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Your user has been created, please login.', category="success")
        return redirect(url_for('account.login'))
    flash('Your user created failed, please try again.', category="error")
    return render_template('register.html',
                           form=form)