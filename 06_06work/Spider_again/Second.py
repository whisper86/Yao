import time
import re
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opt = Options()
web = Chrome(options=opt)

web.get("https://www.hanritai.com/288/#")
time.sleep(2)
Video = web.find_element_by_xpath('/html/body/div[1]/div/div[5]/ul/li[12]/a')
Video.click()

time.sleep(8)
frame = web.find_element_by_xpath('//*[@id="wp1ay"]/div/div[1]/iframe')
web.switch_to.frame(frame)
resp = web.page_source
resp.encode('utf-8')
soup = BeautifulSoup(resp, "html.parser")
r = 'src=".*?vid=(.*?)"'

original_url = re.findall(r, str(soup))[0]
char_url = str(original_url).split("/")
Target_url = char_url[0] + "//" + char_url[1] + '/' + char_url[2] + '/' + char_url[3] + '/' + char_url[4] + '/' + "1000kb/hls/index.m3u8"

print(Target_url)
time.sleep(3)
web.close()
