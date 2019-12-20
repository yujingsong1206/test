from peewee import *


db = MySQLDatabase('spider',
                   host="127.0.0.1",
                   port=3306,
                   user="root",
                   password="123456")


class BaseModel(Model):
    class Meta:
        database = db


class Topic(BaseModel):
    title = CharField() # 题目
    content = TextField(default="") # 内容
    id = IntegerField(primary_key=True) # csdn的id
    author = CharField() # 作者
    create_time = DateTimeField() # 创建日期
    answer_nums = IntegerField(default=0) # 回复数
    click_nums = IntegerField(default=0) # 点击（查看）数
    parised_nums = IntegerField(default=0) # 点赞
    jtl = FloatField(default=0.0) # 结贴率
    score = IntegerField(default=0) # 赏分
    status = CharField() # 状态


class Answer(BaseModel):
    topic_id = IntegerField()
    author = CharField()
    content = TextField(default="")
    create_time = DateTimeField()
    parised_nums = IntegerField(default=0)


class Author(BaseModel):
    name = CharField()
    id = CharField(max_length=30, primary_key=True)
    desc = TextField(null=True)
    follower_nums = IntegerField(default=0) # 粉丝数
    following_nums = IntegerField(default=0) # 关注数


if __name__ == "__main__":
    db.create_tables([Topic, Answer, Author])