#!/usr/bin/env python
# encoding: utf-8

"""
@author: Chenbo
@time: 2018/7/28 11:53
"""
import smtplib
from email.mime.text import MIMEText

from light_blog.config import ACCOUNT, PASSWORD
from light_blog.extensions import flask_celery

from light_blog.model.reminder import Reminder


# @flask_celery.task(   # 了解到该命令中-A参数表示的是Celery APP的名称，这个实例中指的就是tasks.py,
#     # 后面的tasks就是APP的名称，worker是一个执行任务角色，后面的loglevel=info记录日志类型默认是info,
#     # 这个命令启动了一个worker,用来执行程序中add这个加法任务（task）
#     bind=True,
#     igonre_result=True,
#     default_retry_delay=300,
#     max_retries=5)
# def remind(self, primary_key):
#     """Send the remind email to user when registered.
#        Using Flask-Mail.
#     """
#     print("Task is ready!")
#     reminder = Reminder.query.get(primary_key)
#
#     msg = MIMEText(reminder.text)
#     msg['Subject'] = 'Register Success，Congratulations!'
#     msg['FROM'] = ACCOUNT
#     msg['To'] = reminder.email
#     print("正在发送邮件！！！")
#     try:
#         smtp_server = smtplib.SMTP('smtp.qq.com')    # 亲测有效
#         # smtp_server.starttls()
#         smtp_server.login(ACCOUNT, PASSWORD)    # TODO secret care
#         smtp_server.sendmail(ACCOUNT,
#                              [reminder.email],
#                              msg.as_string())
#         smtp_server.close()
#         return
#
#     except Exception as err:
#         self.retry(exc=err)


def on_reminder_save(mapper, connect, self):
    """Callbask for task remind."""
    print("I am working!")
    # remind.apply_async(args=(self.id,), eta=self.date)

    msg = MIMEText("多用户发送测试！")
    msg['Subject'] = 'Register Success，Congratulations!'
    msg['FROM'] = ACCOUNT
    msg['To'] = "1126531273@qq.com"
    print("正在发送邮件！！！")
    try:
        smtp_server = smtplib.SMTP('smtp.qq.com')  # 亲测有效
        # smtp_server.starttls()
        smtp_server.login(ACCOUNT, PASSWORD)  # TODO secret care
        smtp_server.sendmail(ACCOUNT,
                             ["2428986312@qq.com", "2576365182@qq.com", "1126531273@qq.com"],
                             msg.as_string())
        smtp_server.close()
        print("邮件发送完成！")

    except Exception as err:
        print("nice to meet you!")

