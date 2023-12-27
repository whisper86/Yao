from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

opt = Options()
# opt.add_argument("--disable-gpu")
# opt.add_argument('--headless')
# option.add_experimental_option('excludeSwitches', ['enable-automation']
opt.add_argument('--disable-blink-features=AutomationControlled')
web = Chrome(options=opt)
web.maximize_window()

web.get('https://www.baidu.com')

# href = web.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]')
time.sleep(3)
web.find_element_by_xpath('//*[@id="kw"]').send_keys("名侦探柯南", Keys.ENTER)

# print(href.text)

# href.click()

time.sleep(3)
web.switch_to.window(web.window_handles[-1])

for i in range(1, 100):
    web.execute_script('window.scrollTo(0, {});'.format(i * 20))
    time.sleep(0.1)

soup = BeautifulSoup(web.page_source, 'lxml')
log = open("information.txt", mode="a+", encoding="utf-8")
information_list = soup.find_all("div", attrs={"class": "result c-container xpath-log new-pmd"})
for information in information_list:
    information.find("em")
    print(information.text, log.write(f"{information}\t"))
time.sleep(5)
log.close()
web.close()
