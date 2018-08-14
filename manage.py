#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

# 注意以下两个包（app和model)的引入顺序，大坑
# Init manager object via app object
from light_blog.controllers.run import create_app
from light_blog.model import user, post, comment, tag, role
from light_blog import model

env = os.environ.get('BLOG_ENV', 'dev')
app = create_app('light_blog.config.%sConfig' % env.capitalize())

manager = Manager(app)

# Init migrate object via app and db object
migrate = Migrate(app, model.db)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server", Server(host='0.0.0.0', port=6666))
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    """
    Create a python CLI
    :return:  Default import object
    type: 'Dict'
    """
    # 确保有导入Flask app object, 否则启动的CLI上下问中仍然没有app对象
    # return dict(app=run.app)
    return dict(app=app,
                db=model.db,
                User=user.User,
                Post=post.Post,
                Comment=comment.Comment,
                Tag=tag.Tag,
                Role=role.Role)   # post_tag 代表了两张表之间的关联，会由数据库自身来进行处理。

"""
通过manager.py来执行命令行是十分有必要的， 因为一些Flask的扩展只有
在object被创建之后才会被初始化，所以非常依赖应用上下文环境
"""
if __name__ == '__main__':
    manager.run()