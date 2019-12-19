# pip install pymysql
import pymysql

connection = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="123456",
    db="spider",
    charset="utf8mb4"
)

name = "石敢当"
password = "123456"
cursor = connection.cursor()
sql = "insert into users(name, password) values(%s,%s)"
cursor.execute(sql, (name, password))
connection.commit()
cursor.close()
connection.close()

# ORM 对象关系映射
# 1.数据库版本不同 不同的数据库 sql可能语法不同
# 2.便于维护
# 3.sql注入
