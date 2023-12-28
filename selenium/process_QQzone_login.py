from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
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
web.switch_to.default_content()

time.sleep(5)
# iframe1 = web.find_element_by_xpath('//*[@id="login_frame"]')
# web.switch_to.frame(iframe1)
# iframe2 = web.find_element_by_xpath('//*[@id="tcaptcha_iframe_dy"]')
# web.switch_to.frame(iframe2)
# slide_button = web.find_element_by_xpath('//*[@id="tcOperation"]/div[6]')
# ActionChains(web).drag_and_drop_by_offset(slide_button, 120, 0).perform()

