from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()

web.get("https://i.qq.com/")

time.sleep(10)
# 异步加载
# 一共下滑十次，下滑一次停顿0.5s

for i in range(10):
    web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.5)
informations = web.find_elements_by_xpath('//*[@id="feed_friend_list"]')
time.sleep(1)
for information in informations:
    information.find_element_by_tag_name("li")
    print(information.text)


