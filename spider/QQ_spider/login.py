from spider1 import *
import selenium.common.exceptions
from selenium.webdriver import Chrome
import time
import json

web = Chrome()
web.get("https://user.qzone.qq.com/3079593805")
Cookie = open("my_cookies.json", mode="r", encoding="utf-8").read()

cookies = json.loads(Cookie)
web.delete_all_cookies()
time.sleep(2)
for cookie in cookies:
    try:
        # web.add_cookie({
        #     "domain": cookie['domain'],
        #     'expiry': cookie['expiry'],
        #     'httpOnly': cookie['httpOnly'],
        #     'name': cookie['name'],
        #     'path': '/',
        #     'secure': cookie['secure'],
        #     'value': cookie['value']
        # })
        web.add_cookie(cookie)
    except selenium.common.exceptions.InvalidCookieDomainException:
        continue

web.get('https://user.qzone.qq.com')
time.sleep(10)

# web.close()

