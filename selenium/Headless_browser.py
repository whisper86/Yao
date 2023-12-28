from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from shlex import join
import time

import re
# 准备好参数配置
opt = Options
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
# 无头浏览器的配置

web = Chrome(options=opt)

r = "'(/BoxOffice/.*?)'"
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")

# 定位到下拉列
sel_el = web.find_element_by_xpath('//*[@id="OptionDate"]')
# 对元素进行包装，包装成下拉菜单
sel = Select(sel_el)
# 让浏览器调整选项

# 写入到文件
log = open('log.txt', mode='w', encoding='utf-8')
for i in range(len(sel.options)):  # i就是每一个下拉框选项的索引位置
    sel.select_by_index(i)  # 按照索引进行切换
    time.sleep(2)
    tbody = web.find_elements_by_xpath('//*[@id="TableList"]/table/tbody')
    url = web.find_elements_by_class_name("curp")
    for y in tbody:
        name = y.find_elements_by_tag_name("p")
        for Name, x in zip(name, url):
            print(f"{Name.text}", file=log)
            Href = x.get_attribute("onclick")
            # print(Href)

            urllib_list = re.findall(r, Href)
            urllib1 = join(urllib_list)
            urllib2 = eval(urllib1)
            urllib3 = 'https://www.endata.com.cn' + urllib2
            print(f"{urllib3}", file=log)

    # print(f"{tbody.text}\n")  # 打印所有文本信息
    print("==========")
print("运行完毕")
web.close()
log.close()

# 拿到页面源代码(经过数据加载以及JS执行之后的结果的html内容）
# s = web.page_source() 拿到页面源代码
print(web.page_source)

