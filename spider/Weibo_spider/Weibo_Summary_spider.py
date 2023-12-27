from spider2 import *

time.sleep(3)
# information_list = web.find_element_by_xpath('//*[@id="pl_top_realtimehot"]/table/tbody')
href_information = web.find_elements_by_class_name('td-02')

# print(information_list.text)
for href in href_information:
    url = href.find_element_by_tag_name('a').get_attribute("href")
    urllib = href.find_element_by_css_selector()
    title = href.text
    print(title + ":" + url)
