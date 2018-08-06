#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from flask import Flask, redirect, url_for, flash, render_template

import os

from flask_openid import OpenID

from light_blog import config
from light_blog.extensions import bcrypt
from light_blog.forms import LoginForm
from light_blog.route import blog_blueprint, account_blueprint
from light_blog.model import db


def create_app(object_name):
    basedir = os.path.dirname(__file__)

    static_path = os.path.abspath(os.path.join(basedir,  os.path.pardir, 'static'))

    app = Flask(__name__, static_url_path='/static', static_folder=static_path)

    app.config.from_object(object_name)

    # views = __import__('light_blog.route.blog')  #有了蓝本注册之后就不需要import了

    # sqlalchemy绑定app
    db.init_app(app)
    bcrypt.init_app(app)  # bcrypt 也是通过在app注册的
    # login_manager.init_app(app)

    # 重定向至首页目录
    @app.route('/')
    def index():
        return redirect(url_for('blog.home'))

    app.register_blueprint(blueprint=blog_blueprint)
    app.register_blueprint(blueprint=account_blueprint)
    return app


basedir = os.path.dirname(__file__)

static_path = os.path.abspath(os.path.join(basedir,  os.path.pardir, 'static'))

app = Flask(__name__, static_url_path='/static', static_folder=static_path)

app.config.from_object(config.DevConfig)

# views = __import__('light_blog.route.blog')  #有了蓝本注册之后就不需要import了

# sqlalchemy绑定app
db.init_app(app)
bcrypt.init_app(app)  # bcrypt 也是通过在app注册的
openid = OpenID(app, os.path.join(os.path.dirname(__file__), 'tmp'))
# login_manager.init_app(app)


@account_blueprint.route('/login', methods=['GET', 'POST'])
@openid.loginhandler
def login():
    """Veiw function for login."""

    form = LoginForm()

    # openid_form = OpenIDForm()

    if form.validate_on_submit():   # return self.is_submitted() and self.validate()
        # 在登录成功之后会返回 [(‘success’, ‘You have been logged in.’)] 的信息
        flash("You have been logged in.", category="success")
        return redirect(url_for('blog.home'))
    return render_template('login.html',
                           form=form)


# 重定向至首页目录
@app.route('/')
def index():
    return redirect(url_for('blog.home'))


app.register_blueprint(blueprint=blog_blueprint)
app.register_blueprint(blueprint=account_blueprint)

if __name__ == '__main__':
    app.run()
