import json
import time

import selenium.common.exceptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

url = "https://www.aliyundrive.com/sign/in?spm=aliyundrive.index.0.0.2d836f60VmbMo4"
opt = Options()
web = Chrome(options=opt)

with open("aliyun.json", "r", encoding="utf-8") as f:
    cookies = json.load(f)

web.get(url)
web.delete_all_cookies()
time.sleep(2)
# web.maximize_window()
for cookie in cookies:
    try:
        web.add_cookie({
            "domain": cookie['domain'],
            "hostOnly": cookie['hostOnly'],
            "httpOnly": cookie['httpOnly'],
            "name": cookie['name'],
            "path": "/",
            "sameSite": cookie['sameSite'],
            "secure": cookie['secure'],
            "session": cookie['session'],
            "storeId": None,
            "value": cookie['value']
        })
    except selenium.common.exceptions.InvalidArgumentException:
        web.add_cookie({
            "domain": cookie['domain'],
            "hostOnly": cookie['hostOnly'],
            "httpOnly": cookie['httpOnly'],
            "name": cookie['name'],
            "path": "/",
            "secure": cookie['secure'],
            "session": cookie['session'],
            "storeId": None,
            "value": cookie['value']
        })
time.sleep(1)
web.refresh()
