from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()

web.get("https://i.qq.com/",)
time.sleep(2)
iframe = web.find_element_by_xpath('//*[@id="login_frame"]')
web.switch_to.frame(iframe)
mima_login = web.find_element_by_xpath('//*[@id="switcher_plogin"]')
mima_login.click()
time.sleep(1)

user = web.find_element_by_id("u")
user.clear()
user.send_keys("3079593805")
password = web.find_element_by_id("p")
password.clear()
password.send_keys("XuzhongYao2755", Keys.ENTER)
login = web.find_element_by_xpath('//*[@id="login_button"]')
login.click()

time.sleep(10)
iframe = web.find_element_by_xpath('//*[@id="verify"]')
web.switch_to.frame(iframe)
button = web.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[4]/div[2]/div')
button.click()
time.sleep(5)
informations = web.find_elements_by_xpath('//*[@id="feed_friend_list"]/li[2]/ul[1]')
for information in informations:
    information.find_element_by_tag_name("li")
    print(information.text)
