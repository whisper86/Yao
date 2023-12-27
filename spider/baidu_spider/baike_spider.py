import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("--headless")

web = Chrome(options=opt)

web.get("https://baike.baidu.com/item/%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97/3469662?fromModule=lemma_search-box")

width = web.execute_script("return document.documentElement.scrollWidth")

height = web.execute_script("return document.documentElement.scrollHeight")

print(width, height)
web.set_window_size(width, 10000)
time.sleep(2)

web.save_screenshot("baike.png")
