from selenium.webdriver import Chrome
import time
import json

url = "https://login.taobao.com/"

web = Chrome()

web.get(url)
time.sleep(2)
input("扫码登陆后敲回车")

cookies_dict = web.get_cookies()  # 获取当前登陆的cookies信息
cookies_json = json.dumps(cookies_dict)  # cookies信息转化为json格式
# print(cookies_json)

# 登录完成后,将cookies保存到本地文件
out_filename = 'my_cookies.json'
out_file = open(out_filename, 'w', encoding='utf-8')
out_file.write(cookies_json)  # cookies信息保存
out_file.close()

web.close()

