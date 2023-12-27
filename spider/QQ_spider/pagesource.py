# author: yao
# datetime: 11/27/2022
import time
from selenium.webdriver import Chrome

web = Chrome(executable_path="D:\软件（自2021年08月03日）\Google\Chrome\Application\chromedriver.exe")

web.get("https://i.qq.com/")

x = input("扫码登录后按回车")

for i in range(300):  # 慢慢向下滑动窗口，让所有商品信息加载完成
    web.execute_script('window.scrollTo(0, {});'.format(i*100))
    time.sleep(0.1)
time.sleep(3)
web.save_screenshot("Ok.png")
with open("QQ.html", mode="w", encoding='utf-8') as f:
    print(web.page_source, f.write(web.page_source))
