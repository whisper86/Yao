# coding=utf-8
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# 2. Chrome浏览器的版本号大于88
option = Options()
# option.add_experimental_option('excludeSwitches', ['enable-automation']
option.add_argument('--disable-blink-features=AutomationControlled')

web = Chrome(options=option)

web.get("https://kyfw.12306.cn/otn/resources/login.html")

time.sleep(2)
# user 添加用户名（账号）
user = web.find_element_by_xpath('//*[@id="J-userName"]')
user.clear()
user.send_keys("19556394820")

# password 添加密码
password = web.find_element_by_xpath('//*[@id="J-password"]')
password.clear()
password.send_keys("Xuzhongyao2755")

# 点击登陆按键
web.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(2)
# 处理滑动验证 创建事件链
Slide_to_verification = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(Slide_to_verification, 300, 0).perform()  # 注意最后的perform()尤其重要，相当于制定计划后的执行
