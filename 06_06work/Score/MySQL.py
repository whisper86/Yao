import pymysql
from 成绩查询 import Chinese, Math, English, Chemistry, Biology, Physics, All_score, Name

conn = pymysql.connect(host='localhost', user='root', password='Xuzhongyao2755')  # 连接对象（conn），本地则填localhost，用户填root,
# 密码填入自己数据库设定的就行；
cur = conn.cursor()  # 光标对象（cur）
cur.execute("USE class")  # 选择school数据库
for chinese, math, enghish, chemistry, biology, physics, all_score, name in zip(Chinese, Math, English, Chemistry, Biology,Physics, All_score, Name):

    cur.execute(
        "INSERT INTO class.web_student(Name, Chinese, Math, English, Chemistry, Biology, Physics, All_score)"
        "VALUES (%s,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\", \"%s\")",
        (name, chinese, math, enghish, chemistry, biology, physics, all_score))
    cur.connection.commit()  # 用光标进行连接确认

print("Success")  # 在程序中打印查询到的信息
cur.close()  # 先关闭光标；
conn.close()  # 然后再关闭连接，否则会造成连接泄露现象；
