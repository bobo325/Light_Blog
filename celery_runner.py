#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
import os

from celery import Celery

from light_blog.controllers.run import create_app


def make_celery(app):
    """Create the celery process."""

    # Init the celery object via app's configuration.
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'])

    # Flask-Celery-Helper to auto-setup the config.
    # import  pdb
    # pdb.set_trace()
    # cfg = dict([(k.lower(), v) for k, v in app.config.items()])

    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):

        abstract = True    #: If :const:`True` the task is an abstract base class.

        def __call__(self, *args, **kwargs):
            """Will be execute when create the instance object of ContextTask."""

            # Will context(Flask's Extends) of app object(Producer Sit)
            # be included in celery object(Consumer Site).
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    # Include the app_context into celery.Task.
    # Let other Flask extensions can be normal calls.
    celery.Task = ContextTask
    return celery


env = os.environ.get('BLOG_ENV', 'dev')
flask_app = create_app('light_blog.config.%sConfig' % env.capitalize())
# 1. Each celery process needs to create an instance of the Flask application.
# 2. Register the celery object into the app object.
celery = make_celery(flask_app)


# 我们以后会以 CLI 的形式来管理和控制 Celery 的 worker,
# 所以我们将 celery 对象的实现模块放置在 ./celery_runner.py 中,
# 而不是 light_blog/celery_runner.py. Flask app 内部的 tasks
# 任何的定义和实现就交由 Flask-Celery-Helper 来支持就好了,
# 这也是 Flask-Celery-Helper 存在的意义.


# 启动celery命令 celery worker -A celery_runner
