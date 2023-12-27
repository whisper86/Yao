# author: yao
# datetime: 11/26/2022
import json
import time

from selenium import webdriver  # selenium的浏览器控制器
from selenium.webdriver.chrome.options import Options  # 用于设置浏览器启动的一些参数

options = Options()  # 这个选项类似于在Echarts中的Options，都是将相关属性通过键值对的方式组织在一起
# options.add_argument("--headless")  # 不打开浏览器界面，以节省时间
browser = webdriver.Chrome(options=options)  # 初始化一个浏览器控件
browser.get('https://user.qzone.qq.com')
browser.maximize_window()

input("请用手机扫码登录，然后按回车……")  # 等待用手机扫码登录, 登录后回车即可
time.sleep(2)
cookies_dict = browser.get_cookies()  # 获取当前登陆的cookies信息
cookies_json = json.dumps(cookies_dict)  # cookies信息转化为json格式
# print(cookies_json)

# 登录完成后,将cookies保存到本地文件
out_filename = 'my_cookies.json'
out_file = open(out_filename, 'w', encoding='utf-8')
out_file.write(cookies_json)  # cookies信息保存
out_file.close()
print('Cookies文件已写入：' + out_filename)
# browser.get('https://user.qzone.qq.com/')
# time.sleep(10)
browser.close()
