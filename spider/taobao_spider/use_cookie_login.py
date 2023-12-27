import json
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

opt = Options()
opt.add_argument("--disable_gpu")
# option.add_experimental_option('excludeSwitches', ['enable-automation']
opt.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=opt)


url = "https://www.taobao.com/"
web.get(url)

web.delete_all_cookies()

cookies_file = open("my_cookies.json", "r", encoding="utf-8")

cookies = json.load(cookies_file)
for cookie in cookies:
    web.add_cookie({
        'domain': cookie['domain'],
        # 'expiry': cookie['expiry'],
        'httpOnly': cookie['httpOnly'],
        'name': cookie['name'],
        'path': '/',
        'secure': cookie['secure'],
        'value': cookie['value']
    })
web.get(url)
web.set_window_size(1000, 800)
time.sleep(2)
web.find_element_by_xpath('//*[@id="q"]').send_keys("关东煮", Keys.ENTER)

time.sleep(5)

for i in range(20):  # 慢慢向下滑动窗口，让所有视频信息加载完成
    web.execute_script('window.scrollTo(0, {});'.format(i * 50))
    time.sleep(0.1)

# items = web.find_elements_by_class_name("items")
# time.sleep(2)
# for item in items:
#     print(item.text)
soup = BeautifulSoup(web.page_source, "lxml")
items = soup.find_all("div", attrs={"class": "items"})
for item in items:
    # print(item)
    pic = item.find("img")
    print(pic)
time.sleep(6)

web.close()

