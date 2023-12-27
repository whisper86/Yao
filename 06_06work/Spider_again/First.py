import requests
from bs4 import BeautifulSoup

url = "https://www.hanritai.com/288/#"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                  "Safari/537.36 Edg/114.0.1823.43 "
}
resp = requests.get(url, headers=header)
resp.encoding= 'utf-8'
information = BeautifulSoup(resp.text, "html.parser")

print(information.find("div", attrs={"class": "stui-content__detail"}).text)
