import requests

url = "https://pic.mac89.com/pic/202112/06042029_ee6c5e8d4e.jpeg"
alt = "电视节目NCIS" + "." + url.split(".")[-1]
with open(f"最新静态壁纸/{alt}", mode="wb") as f:
    f.write(requests.get(url).content)
