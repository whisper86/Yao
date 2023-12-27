# author: yao
# datetime: 11/26/2022
import json
import time
from datetime import datetime
import selenium.common.exceptions
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("--headless")
# options.add_argument("__disable-gpu")
web = Chrome(options=options, executable_path="D:\软件（自2021年08月03日）\Google\Chrome\Application\chromedriver.exe")

web.get("https://www.zhihu.com")

web.delete_all_cookies()
cookie_filename = "my_cookies.json"
cookies_file = open(cookie_filename, 'r', encoding='utf-8')
cookies = json.load(cookies_file)
for cookie in cookies:
    web.add_cookie({
        'domain': '.zhihu.com',
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None
    })

web.get("https://www.zhihu.com")
time.sleep(1)

vedio_button = web.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div[1]/div/div[1]/nav/a[4]')
vedio_button.click()
time.sleep(1)

f = open("vedio3.txt", 'a+', encoding='utf-8')
print("知乎视频：", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=f)

open_buttons = web.find_elements_by_class_name('css-1tane06')  # 每一个vedio_title包含一个视频的Link的所有信息，不仅仅为title
open_buttons2 = web.find_elements_by_class_name('css-cazg48')
for open_button, open_button2 in zip(open_buttons, open_buttons2):
    def video1():
        # 打印出每个视频出处的url
        url_title = open_button.find_element_by_tag_name('a').get_attribute('href')
        print(url_title, f.write(f"{url_title}\n"))
        open_button.click()
        time.sleep(2)
        web.switch_to.window(web.window_handles[-1])
        try:
            url = web.find_element_by_xpath('//*[@id="ali_player_0"]').find_element_by_tag_name('video')
        except selenium.common.exceptions.NoSuchElementException:
            url = web.find_element_by_xpath('//*[@id="player"]/div/div/div[1]').find_element_by_tag_name('video')
        else:
            pass
        try:
            title = web.find_element_by_xpath('//*[@id="root"]/div/main/article/div[1]/div[4]/div[1]/div/h1')
        except selenium.common.exceptions.NoSuchElementException:
            title = web.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/div[2]/div/div[1]/div[1]/h1')
        title = title.text
        urllib = url.get_attribute('src')
        print(f"{urllib}\n", f.write(f"{urllib}\n"))
        print(f"{title}\n", f.write(f"{title}\n"))
        web.close()
        web.switch_to.window(web.window_handles[0])
    video1()


    def video2():
        # 打印出每个视频出处的url
        url_title = open_button.find_element_by_tag_name('a').get_attribute('href')
        print(url_title, f.write(f"{url_title}\n"))
        open_button2.click()
        time.sleep(2)
        web.switch_to.window(web.window_handles[-1])
        try:
            url = web.find_element_by_xpath('//*[@id="ali_player_0"]').find_element_by_tag_name('video')
        except selenium.common.exceptions.NoSuchElementException:
            url = web.find_element_by_xpath('//*[@id="player"]/div/div/div[1]').find_element_by_tag_name('video')
        else:
            pass
        urllib = url.get_attribute('src')
        try:     # 话题内容的标题
            title = web.find_element_by_xpath('//*[@id="root"]/div/main/article/div[1]/div[4]/div[1]/div/h1')
        except selenium.common.exceptions.NoSuchElementException:
            title = web.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/div[2]/div/div[1]/div[1]/h1')
        title = title.text
        print(f"{urllib}\n", f.write(f"{title}\n"))
        print(f"{title}\n", f.write(f"{title}\n"))
        web.close()
        web.switch_to.window(web.window_handles[0])

    video2()
f.close()
