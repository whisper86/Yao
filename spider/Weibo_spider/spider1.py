import time
import json
from selenium.webdriver import Chrome

web = Chrome()

url = "https://weibo.com"

web.get(url)
web.delete_all_cookies()

input("扫码登陆后按回车")

cookie = web.get_cookies()

with open("My_cookie.json", mode="w", encoding="utf-8") as f:
    f.write(json.dumps(cookie))
    print("Cookies has saved")
time.sleep(5)

web.close()
