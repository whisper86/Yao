from selenium.webdriver import Chrome
import time
web = Chrome()
# 如果页面中遇到了iframe如何处理
web.get("https://i.qq.com/")

time.sleep(2)
# 其中QQ动态的密码登陆选项在iframe中
# 处理iframe的话，必须先拿到iframe，然后切换视角到iframe，之后才可以拿到数据
iframe = web.find_element_by_xpath('//*[@id="login_frame"]')
web.switch_to.frame(iframe)  # 将selenium的视角转到iframe中
mima_login = web.find_element_by_xpath('//*[@id="switcher_plogin"]')
mima_login.click()
# 将selenium视角切换到主页面（默认页面）
web.switch_to.default_content()  # 不常用
