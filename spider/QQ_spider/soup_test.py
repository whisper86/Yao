# author: yao
# datetime: 11/27/2022
from bs4 import BeautifulSoup

with open("QQ.html", mode="r", encoding="utf-8") as f:
    information = f.read()
    soup = BeautifulSoup(information, "html.parser")

    info_list = soup.find_all("div", attrs={"class": "f-info"})
    for info in info_list:
        print(info.text)
# 以上的代码（QQ.html）的内容并不全

