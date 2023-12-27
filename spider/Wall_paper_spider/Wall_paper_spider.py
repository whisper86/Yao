from lxml import etree
from bs4 import BeautifulSoup
import requests

headers = {
    "User_Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Mobile Safari/537.36 "
}
url = "https://www.macw.com/bzlist/"
resp = requests.get(url)

resp_html = etree.HTML(resp.text)

html = etree.tostring(resp_html, encoding='utf-8').decode()

soup = BeautifulSoup(html, "lxml")

sec_title_list = soup.find_all("div", attrs={"class": "sec-title"})
for sec_title in sec_title_list:
    title = sec_title.find("h2")
    new_title = str(title).split(">")[1]
    new_title2 = new_title.split("<")[0]
    print(new_title2)
    # os.mkdir(f"{new_title2}")
    href = sec_title.find("a").get("href")
    print("https://www.macw.com" + href)
    # child_page_spider
