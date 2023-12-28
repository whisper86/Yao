# 能不能让我的程序连接到浏览器， 让浏览器来完成各种复杂的操作，我们只接受最终的结果
# selenium： 自动化测试工具
# 可以：打开浏览器，然后像人一样操作浏览器
# 程序员可以从selenium中直接提取到网页上的各种信息
# 环境搭建：
#    pip install selenium -i 清华源
#     下载浏览器驱动
#     把解压的浏览器驱动chromedriver放在python解释器的文件夹
# 让selenium启动谷歌浏览器
from selenium.webdriver import Chrome
from selenium import webdriver
import time

# 1.创建浏览器对象
# web = Chrome()
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# web = webdriver.Remote(
#     command_executor="http://192.168.2.141:4444/wd/hub",
#     desired_capabilities=DesiredCapabilities.CHROME
# )
web = Chrome()
# 2.打开一个网址
web.get("https://www.baidu.com")

print(web.title)
# 3.核心思想
#  通过代码模仿人类操作
time.sleep(2)
web.close()
web.quit()

