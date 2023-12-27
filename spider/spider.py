import requests

url = "https://hao.360.com/"
header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/106.0.0.0 Safari/537.36"}
resp = requests.get(url, headers=header)
fp = open('test.txt', "w")
print(resp.text, file=fp)
