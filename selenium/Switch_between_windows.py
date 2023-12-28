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
web.find_element_by_xpath('//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
# 如何进入到窗口进行提取
# 注意在selenium中，新窗口是不切换过来的
web.switch_to.window(web.window_handles[-1])  # -1表示最后一个窗口

# 在新窗口提取内容
time.sleep(3)
information = web.find_element_by_xpath('//*[@id="job_detail"]')
print(information.text)

# 关掉子窗口
web.close()
# 注意此时的selenium视角依然是被关掉的那个窗口
# 变更selenium 的窗口视角，回到原来的窗口中 
web.switch_to.window(web.window_handles[0])
