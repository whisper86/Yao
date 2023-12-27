# author: yao
# datetime: 11/26/2022
import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = Options()
# options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

browser.get("https://i.qq.com/")
time.sleep(5)

# browser.save_screenshot("QQ_login.png") # 保存图片

wait = WebDriverWait(browser, 10)
for i in range(300):  # 慢慢向下滑动窗口，让所有商品信息加载完成
    browser.execute_script('window.scrollTo(0, {});'.format(i*100))
    time.sleep(0.1)

wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="feed_friend_tips"]/div/p')), message="wait hotlist loading")  # 等待页面底部的当前页码出现
# browser.save_screenshot("QQ_end.png")

page_source = browser.page_source

soup = BeautifulSoup(page_source, "html.parser")

img_list = soup.select('img')
for img in img_list:
    src = img.get('src')
    print(src)
