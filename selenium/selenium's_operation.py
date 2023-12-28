from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
web = Chrome()

web.get("http://lagou.com")

# 找到某个元素， 点击它

button = web.find_element_by_xpath('//*[@id="changeCityBox"]/ul/li[2]/a')
button.click()

time.sleep(1)
# 找到输入框， 输入python => 输入回车/点击搜索回车
web.find_element_by_xpath('//*[@id="search_input"]').send_keys("python", Keys.ENTER)

time.sleep(2)
# 查找存放数据的位置，进行数据提取
# 找到页面存放数据的所有数据的class="item_10RTO"
elements = web.find_elements_by_xpath('//*[@id="jobList"]/div[1]')
for element in elements:
    element.find_element_by_tag_name("a")
    print(element.text)
