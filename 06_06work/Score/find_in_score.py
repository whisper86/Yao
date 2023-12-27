# 作者：许垚
# 开发时间2022年10月08日
from 成绩查询 import Name
from bs4 import BeautifulSoup
import webbrowser

print("*********成绩查询系统***********")
# 浏览器运行目录
chromePath = r"D:\软件（自2021年08月03日）\Google\Chrome\Application\chrome.exe"

# 注册浏览器
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
Flag = True
while Flag:
    name = input("请输入你想要查找的学生姓名(Enter 'q' to exit")
    if name not in Name and name != "q":
        print("查无此人，你确定你所查找的学生位于class 12？")
    elif name == "q":
        Flag = False
        break
    else:
        # 获取浏览器并打开指定地址
        webbrowser.get('chrome').open(f"file:///F:/PycharmProjects/Score/{name}'s%20academic%20performance.html", new=1,
                                      autoraise=True)
