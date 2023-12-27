# Auther: Yao
# Datetime: 2022.10.24

import os
import time

import requests
from bs4 import BeautifulSoup
import re
import book_spider
from time import sleep
header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
                        "like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"}
Url = book_spider.Url
Title = book_spider.Title

r = 'src="(.*?.jpeg.*?)"'
for URL, title in zip(Url, Title):
    url = URL
    # os.mkdir(title)
    # time.sleep(3)
    resp = requests.get(url, headers=header)

    # print(resp.text)
    soup = BeautifulSoup(resp.text, "html.parser")
    result = soup.findAll("img")
    for i, x in zip(result,range(1,134)):
        urllib = re.findall(r, str(i))
        for urllib2 in urllib:
            url0 = "https:" + urllib2 + "/format,webp"
            name = str(url0)
            print(url0)

            # with open(f"/Users/yao/PycharmProjects/pythonProject/spider/{title}/{name}.jpg", mode="wb") as f:
            picture = requests.get(url0, headers=header)
            with open(f"{x}.jpg", mode="wb")as f:
                f.write(picture.content)
