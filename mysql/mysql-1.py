# coding=utf-8


# 确保 python 版本一致 3.x
import pymysql

# 连接数据库
connection = pymysql.connect("localhost", "root", "199011081108", "python")
print (connection)
# 获取操作游标
cursor = connection.cursor()
print (cursor)
# 获取一条数据
sql = 'SELECT * FROM user'
cursor.execute(sql)
first_data = cursor.fetchone()
print (first_data)
left_data = cursor.fetchall()
print (left_data)
# insert_sql = "INSERT INTO user(id, username) VALUES ('10', '10lee')"
# cursor.execute(insert_sql)
update_sql = "UPDATE user SET username = '20lee' WHERE id = '10'"
cursor.execute(update_sql)
print (cursor.rowcount)
delete_sql = "delete from user WHERE id = '1'"
cursor.execute(delete_sql)
connection.commit()
cursor.close()
connection.close()
