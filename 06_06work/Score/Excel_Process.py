import pandas as pd
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='Xuzhongyao2755')  # 连接对象（conn），本地则填localhost，用户填root,
# 密码填入自己数据库设定的就行；
cur = conn.cursor()  # 光标对象（cur）
cur.execute("USE yao")  # 选择school数据库

file_path = r"C:\Users\xu\OneDrive\文档\Film_Information.xlsx"  # r对路径进行转义，windows需要
raw_data = pd.read_excel(file_path, header=0)  # header=0表示第一行是表头，就自动去除了
# print(raw_data)
data = raw_data.values  # 只提取表中信息
# print(data[0])
All_information = []
for information in data:
    # print(information)
    # print("\n")
    for more_information in information:
        # print(more_information)
        # print("\n")
        All_information.append(more_information)

# print(All_information)
Title = [0] + [5 * i for i in range(1, 19)] + [95]
Url = [1] + [5 * i + 1 for i in range(1, 19)] + [96]
Type = [3] + [5 * i + 3 for i in range(1, 19)] + [98]
Region = [4] + [5 * i + 4 for i in range(1, 19)] + [99]
for t1, u, t2, r in zip(Title, Url, Type, Region):
    title = All_information[t1]
    url = All_information[u]
    type = All_information[t2]
    region = All_information[r]
    # print(url)
    cur.execute(
        "INSERT INTO yao.film_information(Title, Url, Type, Region) "
        "VALUES (%s,\"%s\",\"%s\",\"%s\")",
        (title, url, type, region))
    cur.connection.commit()  # 用光标进行连接确认
print("Success")
