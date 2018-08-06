"""
用于生产假数据
@Author:ChenBo
"""
import random
import datetime

from light_blog.model import db
from light_blog.model.post import Post
from light_blog.model.role import Role
from light_blog.model.user import User
from light_blog.model.tag import Tag


user1 = User(username='bobo测试', password='bobo测试')
user2 = User(username="bobo", password="bobo")
db.session.add(user1)
db.session.add(user2)
db.session.flush()
role = Role(name="初始化角色")
role2 = Role(name="bobo角色2")
user1.role = [role, role2]
user2.role = [role, role2]
db.session.add(role)
db.session.add(role2)
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
