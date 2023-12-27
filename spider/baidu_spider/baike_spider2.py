import time
from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait

# opt = Options()
# opt.add_argument("--headless")

web = Chrome()

web.get("https://baike.baidu.com/item/%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97/3469662?fromModule=lemma_search-box")

# width = web.execute_script("return document.documentElement.scrollWidth")
#
# height = web.execute_script("return document.documentElement.scrollHeight")

# print(width, height)
# web.set_window_size(width, 10000)
time.sleep(2)
wait = WebDriverWait(web, 10)
for i in range(3):  # 慢慢向下滑动窗口，让所有商品信息加载完成
    web.execute_script('window.scrollTo(0, {});'.format(i*100))
    time.sleep(0.1)
wait.until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/div[9]/dl[1]/dd[1]')), message="wait hotlist loading")  # 等待页面底部的当前页码出现
web.save_screenshot("basic_info2.png")