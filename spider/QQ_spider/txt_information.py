# author: yao
# datetime: 11/27/2022
import re

r = "([\u4e00-\u9fa5].*?)<"

with open("QQ.html", mode='r', encoding='utf-8')as f:
    information = f.read()
    txt = re.findall(r, information)
    for text in txt:
        print(txt)