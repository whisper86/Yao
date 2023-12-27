import requests
from bs4 import BeautifulSoup
url_list = ['https://wap.umei.cc/meinvtupian/siwameinv/234042.htm', "https://wap.umei.cc/meinvtupian/siwameinv/234041.htm"]
alt_list = ["黑丝", "辣妹"]
# https://wap.umei.cc/meinvtupian/siwameinv/241438.htm
for url, alt in zip(url_list, alt_list):
    # url = 'https://wap.umei.cc/meinvtupian/siwameinv/235685.htm'
    resp = requests.get(url)
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, "html.parser")
    image = soup.find("li", attrs={"class": "tal"}).find("img").get("src")

    image_list = soup.find("a", attrs={"class": "noclick"})
    print(url)
    print(image)
    with open(f"{alt}_0.jpg", mode="wb") as f:
        img = requests.get(f"{image}").content
        f.write(img)
    # print(image_list.text.split("/")[1])
    n = 1
    num = image_list.text.split("/")[1]
    for i in range(2, int(num) + 1):
        urllib = url.split(".")
        # print(url)
        new_url1 = urllib[0] + "."
        new_url2 = urllib[1] + "."
        new_url3 = urllib[2] + f"_{i}."
        urllib[2] = new_url3
        new_str = new_url1 + new_url2 + new_url3 + urllib[3]
        print(new_str)
        resp2 = requests.get(f"{new_str}")
        resp2.encoding = "utf-8"
        soup2 = BeautifulSoup(resp2.text, "html.parser")
        image = soup2.find("li", attrs={"class": "tal"}).find("img").get("src")
        print(image)
        with open(f"{alt}_%s.jpg" % n, mode="wb") as f:
            img = requests.get(f"{image}").content
            f.write(img)
            n += 1  # n自增1
