#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("148.70.67.47", "xiaofang", "xiaofang1!", "vue_admin", charset='utf8mb4')
# db = MySQLdb.connect("127.0.0.1", "root", "123123", "test", charset='utf8mb4')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute()方法执行SQL语句
sql = "select id,title from article"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    res = []
    for row in results:
        print(row)

except:
    print("error")

# print(res)

db.close()
