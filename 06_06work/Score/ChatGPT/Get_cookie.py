import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

web = Chrome(executable_path="D:\软件（自2021年08月03日）\Google\Chrome\Application\chromedriver.exe")
opt = Options()
# opt.add_experimental_option('excludeSwitches', ['enable-automation']
opt.add_argument('--disable-blink-features=AutomationControlled')
web.get("https://chat.openai.com/chat")

#  验证浏览器环境， 真人测试
time.sleep(20)
Button = web.find_element(By.XPATH, '//*[@id="cf-stage"]/div[6]/label/span')
time.sleep(2)
Button.click()

#  完成人机测试，点击Log in，发送账号和密码，清除browser原有cookie， 获取Chat GPT Cookie
time.sleep(2)
Login_button = web.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div[4]/button[1]')
Login_button.click()
