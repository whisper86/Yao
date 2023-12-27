# import os
import time
import spider2
from bs4 import BeautifulSoup
# from selenium.webdriver import Chrome
# os.system("spider2.py")

# web = Chrome()
web = spider2.web
time.sleep(3)
for i in range(100):
    web.execute_script('window.scrollTo(0, {});'.format(i * 50))
    time.sleep(0.1)
Items = web.find_elements_by_class_name("vue-recycle-scroller__item-view")
# for item in Items:
#     item.find_element_by_class_name("detail_wbtext_4CRf9")
#     print(item.text)
# item = spider2.web.find_element_by_xpath('//*[@id="scroller"]/div[1]/div[3]/div/article/div[2]/div/div/div')
# print(item.text)

soup = BeautifulSoup(web.page_source, 'html.parser')

wbtext_list = soup.find_all('div', attrs={"class": "detail_wbtext_4CRf9"})

for wbtext in wbtext_list:
    print(wbtext)
