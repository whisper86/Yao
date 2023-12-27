# author: yao
# datetime: 11/26/2022
import json
import time
from datetime import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from threading import Thread

options = Options()
# options.add_argument("--headless")
web = Chrome(options=options, executable_path="D:\软件（自2021年08月03日）\Google\Chrome\Application\chromedriver.exe")

web.get("https://www.zhihu.com")
web.maximize_window()

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
time.sleep(5)

vedio_button = web.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div[1]/div/div[1]/nav/a[4]')
vedio_button.click()

wait = WebDriverWait(web, 10)
for i in range(100):  # 慢慢向下滑动窗口，让所有视频信息加载完成
    web.execute_script('window.scrollTo(0, {});'.format(i * 100))
    time.sleep(0.1)

wait.until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="TopstoryContent"]/div/div[1]/div[78]')), message="wait hotlist loading")  # 等待页面底部的当前页码出现
web.save_screenshot("zhihu_vedio.png")

f = open("vedio.txt", 'w', encoding='utf-8')
print("知乎视频：", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=f)

soup = BeautifulSoup(web.page_source, 'html.parser')


def spider1():
    open_buttons = web.find_elements_by_css_selector(".css-1tane06")
    for vedio_title1, open_button in zip(soup.select('.css-1tane06'),
                                         open_buttons):  # 每一个vedio_title包含一个视频的Link的所有信息，不仅仅为title
        vedio_title1.select('.css-tfs9zi')
        open_button.click()
        print(vedio_title1.text)
        web.switch_to_window(web.window_handles[1])


def spider2():
    for vedio_title2 in soup.select('.css-cazg48'):
        vedio_title2.select('h2')
        print(vedio_title2.text)


thread_list = [
    Thread(target=spider1()),
    Thread(target=spider2())
]


def main():
    # 启动三个线程
    for thread in thread_list:
        thread.start()
    # 等待线程结束
    for thread in thread_list:
        thread.join()


if __name__ == "__main__":
    main()
