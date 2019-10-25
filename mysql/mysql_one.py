# coding=utf-8


# 确保 python 版本一致 3.x
import pymysql

def run():
    # 连接数据库
    connection = pymysql.connect("rm-uf638ac07s28ra89po.mysql.rds.aliyuncs.com", "afcsu185766348", "pw85BhfmE75#8Fh3ebv", "afcsdbkd8t75vfh79")
    print(connection)
    # 获取操作游标
    # cursor = connection.cursor()
    # print(cursor)
    # # 获取一条数据
    # sql = 'SELECT * FROM user'
    # cursor.execute(sql)
    # first_data = cursor.fetchone()
    # print(first_data)
    # left_data = cursor.fetchall()
    # print(left_data)
    #
    # print(cursor.rowcount)
    #
    # connection.commit()
    # cursor.close()
    # connection.close()


if __name__ == '__main__':
    run()