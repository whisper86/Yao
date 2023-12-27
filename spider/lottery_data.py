import requests
from bs4 import BeautifulSoup

url = "https://datachart.500.com/ssq/history/history.shtml"

resp = requests.get(url)
resp.encoding = "gbk"

soup = BeautifulSoup(resp.text, "lxml")

data = soup.find("tbody", attrs={"id": "tdata"})
DATA = []
with open("data.csv", mode="w", encoding="utf-8") as f:
    for number in data:
        number_data = number.find_all_next("tr", attrs={"class": "t_tr1"})
        for data in number_data:
            # print(f"{data.text}\t")
            for Number in data:
                print(f"{Number.text}")
                DATA.append(Number.text)
        for result in DATA:
            print(result, f.write(result))
            print("这是其中的一期内容")
