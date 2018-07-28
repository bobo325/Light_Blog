#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
from flask_script import Manager, Server

import app

manager = Manager(app.app)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    """
    Create a python CLI
    :return:  Default import object
    type: 'Dict'
    """
    # 确保有导入Flask app object, 否则启动的CLI上下问中仍然没有app对象
    return dict(app=app.app)

"""
通过manager.py来执行命令行是十分有必要的， 因为一些Flask的扩展只有
在object被创建之后才会被初始化，所以非常依赖应用上下文环境
"""
if __name__ == '__main__':
    manager.run()