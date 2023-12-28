import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
    command_executor = 'http://192.168.2.4:4444/wd/hub',
    desired_capabilities = DesiredCapabilities.CHROME
)

driver.get('https://www.baidu.com')
time.sleep(1)
driver.close(), driver.quit()