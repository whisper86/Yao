# 1. 图像识别
# 2. 选择互联网上成熟的验证码工具

from selenium.webdriver import Chrome
from chaojiying import Chaojiying_Client
import time

web = Chrome()

web.get("https://www.chaojiying.com/user/login/")
time.sleep(2)

# 向页面添加用户名
user = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input')
user.clear()
user.send_keys("19556394820")
# 向页面添加密码
password = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input')
password.clear()
password.send_keys("Xuzhongyao2755")
# 向页面添加验证码
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('19556394820', 'Xuzhongyao2755', '941053')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']

verify_code_input = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input')
verify_code_input.clear()
verify_code_input.send_keys(verify_code)

# 点击登陆
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()

