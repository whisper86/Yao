from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

# 准备好参数配置
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
# 无头浏览器的配置

web = Chrome(options=opt)

web.get("https://qzone.qq.com/")
time.sleep(2)

# 如何拿到页面代码（经过数据加载和JS处理之后的html内容
print(web.page_source)
