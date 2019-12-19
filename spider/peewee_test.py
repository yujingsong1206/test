# pip install peewee
# http://docs.peewee-orm.com/en/latest/index.html
from peewee import *

db = MySQLDatabase('spider',
                   host="127.0.0.1",
                   port=3306,
                   user="root",
                   password="123456")


class Users(Model):
    name = CharField()
    password = CharField()

    class Meta:
        database = db
        # table_name = "haha"


if __name__ == "__main__":
    db.create_tables([Users])

    # 插入数据
    # user = Users(name="小明", password="456")
    # user.save()

    # 查询数据(一条)
    # user = Users.select().where(Users.name == '小明').get()
    # print(user.id)

    # 查询数据（所有）
    # query = Users.select().where(Users.name == '小明')
    # for user in query:
    #     print(user.id, user.name)

    # 修改数据
    # user = Users.select().where(Users.name == '小明').get()
    # user.password = "789456123"
    # user.save()

    # 删除数据
    # query = Users.select().where(Users.name == "小铭铭")
    # for user in query:
    #     user.delete_instance()