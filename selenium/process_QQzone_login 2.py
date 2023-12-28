from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# # 2. Chrome浏览器的版本号大于88
# option = Options()
# # option.add_experimental_option('excludeSwitches', ['enable-automation']
# option.add_argument('--disable-blink-features=AutomationControlled')

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

iframe1 = web.find_element_by_xpath('//*[@id="login_frame"]')
web.switch_to.frame(iframe1)
iframe2 = web.find_element_by_xpath('//*[@id="verify"]')
web.switch_to.frame(iframe2)
# 发送验证码
web.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[4]/div[2]/div').click()
time.sleep(20)
# 进入到QQ动态主页
web.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div[5]/button/div').click()
time.sleep(3)
web.switch_to.window(web.window_handles[-1])

# 一共下滑十次，下滑一次停顿0.5s

for i in range(10):
    web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.5)
    informations = web.find_elements_by_xpath('//*[@id="feed_friend_list"]')
    for information in informations:
        information.find_element_by_tag_name("li")
        print(information.text)
