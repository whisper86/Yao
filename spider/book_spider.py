# Auther: Yao
# Datetime: 2022.10.24

import re
from bs4 import BeautifulSoup
import requests

url = "https://www.ihuaben.com/book/3897068.html"

r = 'href="(.*?.html)"'
r2 = 'title="(.*?)"'

resp = requests.get(url)

soup = BeautifulSoup(resp.text, "html.parser")

# print(soup)
result = soup.findAll("p")
# print(result)
result2 = re.findall(r, str(result))
result3 = re.findall(r2, str(result))
# print(result2)
result5 = result3[:-4]
result4 = result2[:-4]
# print(len(result4))
Url = []
Title = []
for i, i2 in zip(result4, result5):
    urllib = "https:" + i
    # print(urllib)
    # print(i2)
    Url.append(urllib)
    Title.append(i2)


