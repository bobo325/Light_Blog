"""
用于生产假数据
@Author:ChenBo
"""
import random
import datetime

from light_blog.model import db
from light_blog.model.post import Post
from light_blog.model.user import User
from light_blog.model.tag import Tag


user = User(username='bobo测试', password='bobo测试')
db.session.add(user)
db.session.flush()

user = db.session.query(User).first()
tag_one = Tag(name='Python')
tag_two = Tag(name='Flask')
tag_three = Tag(name='SQLALchemy')
tag_four = Tag(name='JMilkFan')
db.session.add(tag_one)
db.session.add(tag_two)
db.session.add(tag_three)
db.session.add(tag_four)
db.session.flush()
tag_list = [tag_one, tag_two, tag_three, tag_four]

s = "EXAMPLE TEXT"

for i in range(100):
    new_post = Post(title="Post" + str(i), publish_date=datetime.datetime.now(),
                    user_id=user.id, text=s)
    tags = random.sample(tag_list, random.randint(1, 3))

    # for tag in tags:
    #     new_post.tag.append(tag)  # 问题，不能生产数据
    new_post.tag = tags
    db.session.add(new_post)

db.session.commit()
