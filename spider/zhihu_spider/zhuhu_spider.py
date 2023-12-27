# # author: yao
# # datetime: 11/26/2022
#
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# import requests
#
# # 2. Chrome浏览器的版本号大于88
# option = Options()
# # option.add_experimental_option('excludeSwitches', ['enable-automation']
# option.add_argument('--disable-blink-features=AutomationControlled')
#
# url = "https://www.zhihu.com/"
# web = Chrome(executable_path="D:\软件（自2021年08月03日）\Google\Chrome\Application\chromedriver.exe")
# heads = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/100.0.4896.127 Safari/537.36 ",
#     "cookie": "_zap=eefa297c-0407-4176-8706-75c780eae47f; _xsrf=8a91afb5-6788-4d89-bddf-ff8eea3938c8; "
#               "d_c0=ABBYO3XvrBWPTmYe692NMVeQAUyFNFPbdMY=|1665162749; _9755xjdesxxd_=32; "
#               "YD00517437729195:WM_TID=9COFS0u98BFEBAFVAULETo+oX1iK5ixG; "
#               "YD00517437729195:WM_NIKE"
#               "=9ca17ae2e6ffcda170e2e6eea5d47a8eacfaa7ef3b87a88fa6d14b978f9fb0d160b3bf9e97ea43bcb8fd8ae52af0fea7c3b92a908daa82b449bbb1fd9bc63caaec8fd8e452a9f1f9d4d33c838c87d1d562a1f18498fc7b96f1e58dd06b90eb0093ae4ba8af828ee17c909fa8ccd154948fbba3d65ea99eff92dc748beafbb4b234a9a68e82cd3b8586ae8ee473ba98be92c774bbb2fa8ad147f3939dd7ee49edb9baadc939bcbdc0d5f97ba3f59fd5d069b7b7ab8eb737e2a3; YD00517437729195:WM_NI=LSfa1Cyo3zG0j4A7aZk/73P0ATI0Vjc/LwyqV/+lMaL50r/AdqNmbpLAh+RXPQuBWVkB1qYxI65S38kzBaN1GZbmayzHrqDxyn6iRM1MS6oC/gvLJ3xcp4zqa+Q4Mcuiem4=; __snaker__id=Z3gk6q8vEhG98jKd; gdxidpyhxdE=uKD7biTOwi7KWnPi1Z0rsUBDEYM3eTuNK66XAeRrzY\epsuhJTPXntOjDmN00+KjCIfORrBZV0a1rHi6h2s++WbUAtr/Rp90HNR4oQ+tpTWhXrKWRtVVpl+RNjzfarm+UDOYlv0GJ3zK0\4\jp\StLKAbq7SbIGpudraHdenJ2\KiWtA:1665830407219; o_act=login; utm_source=so; ref_source=other_https://www.zhihu.com/signin?next=/; expire_in=15552000; q_c1=e2aed945c0ed4339a0d1e33cc9c317a3|1665829548000|1665829548000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1668268405; z_c0=2|1:0|10:1669013443|4:z_c0|80:MS4xczJrdUdRQUFBQUFtQUFBQVlBSlZUY050YUdRc0ctc0tETHptTmJpeXFqWEYwa2dZQzlxWXFBPT0=|3c02d06e1488616b96617da2486212e2dcdddde858c38413b4143f76f341ec68; tst=r; SESSIONID=JWJrbmMo2pWHNedXwknW9rzRqDuotICRNFgDiuEahgS; JOID=Vl0SC0sp35i-F6V7QCVKA2NoRtJWYordxHHJNCAfrs35UcQeGl7aHtESpnZHfJp6sJE-Sm5dINa0Y69X7sRp5kE=; osd=W1scB0wk2ZayEKh9TilNDmVmStVbZITRw3zPOiwYo8v3XcMTHFDWGdwUqHpAcZx0vJYzTGBRJ9uybaNQ48Jn6kY=; KLBRSID=af132c66e9ed2b57686ff5c489976b91|1669401377|1669400685; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1669401380 "
# }
#
# web.get(url)
#
# page_source = web.page_source
# resp = requests.get(url, headers=heads)
# resp.encoding = "utf-8"
# print(page_source)
# print(resp.text)

import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = Options()
# options.add_argument("--headless")
# browser = webdriver.Chrome(options=options,executable_path="D:\软件（自2021年08月03日）\Google\Chrome\Application\chromedriver.exe")
browser = webdriver.Chrome(options=options)

browser.get("https://www.zhihu.com")
browser.maximize_window()


browser.delete_all_cookies()
cookie_filename = "my_cookies.json"
cookies_file = open(cookie_filename, 'r', encoding='utf-8')
cookies = json.load(cookies_file)
for cookie in cookies:
    browser.add_cookie({
        'domain': '.zhihu.com',
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None
    })

browser.get("https://www.zhihu.com")
time.sleep(3)

browser.save_screenshot("zhihu_login.png") # 保存图片

hot_button = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div[1]/div/div[1]/nav/a[3]')
hot_button.click()


wait = WebDriverWait(browser, 10)
for i in range(100):  # 慢慢向下滑动窗口，让所有商品信息加载完成
    browser.execute_script('window.scrollTo(0, {});'.format(i*100))
    time.sleep(0.1)

wait.until(EC.presence_of_element_located(
    (By.XPATH, '//div[@class="HotList-end"]')), message="wait hotlist loading")  # 等待页面底部的当前页码出现
browser.save_screenshot("zhihu_hot.png")

f = open("hot.txt", 'w', encoding='utf-8')
print("知乎热榜：", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=f)

soup = BeautifulSoup(browser.page_source, 'html.parser')
for item in soup.select("section.HotItem"):
    item_index = item.select("div.HotItem-rank")
    print(item_index[0].get_text(), file=f)
    item_title = item.select("h2.HotItem-title")
    print("问题：", item_title[0].get_text(), file=f)
    item_excerpt = item.select("p.HotItem-excerpt")
    if len(item_excerpt):
        print("概述：",item_excerpt[0].get_text(), file=f)
    item_metrics = item.select("div.HotItem-metrics")
    print("热度：",item_metrics[0].get_text()[:-7] + "万", file=f)
