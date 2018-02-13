# coding=utf-8


# 确保 python 版本一致 3.x
import pymysql

# 连接数据库
db = pymysql.connect("localhost", "root", "199011081108", "python")

# 获取操作游标
curse = db.cursor()

curse.execute("SELECT VERSION()")
# curse.execute("SHOW TABLES")
# 获取一条数据
data = curse.fetchone()

print data

db.close()
