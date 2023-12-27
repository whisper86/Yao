import time
import json
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--headless")
opt.add_argument('--disable-gpu')
web = Chrome(options=opt)

url = "https://weibo.com"

web.get(url)
web.delete_all_cookies()

Cookie = open("My_cookie.json", mode="r", encoding="utf-8").read()
cookies = json.loads(Cookie)

for cookie in cookies:
    web.add_cookie(cookie)

# web.get("https://weibo.com/n/%E4%B8%80%E5%8F%AA%E7%89%B9%E7%AB%8B%E7%8B%AC%E8%A1%8C%E7%9A%84%E6%9C%B1v")
web.get("https://s.weibo.com/top/summary?cate=realtimehot&luicode=30000490&lfid=HW_fuyiping_feedresou&wm=20004_90009"
        "&launchid=30000490-HW_fuyipingfeedresou&backtothirdpage=1&callparam=hw_qjs_return")
