import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.umei.cc/meinvtupian/siwameinv/")

resp.encoding = "utf-8"

# print(resp.text)

main_page = BeautifulSoup(resp.text, "html.parser")
# soup的查找用法
image_list = main_page.find("div", attrs={"class": "item_list infinite_scroll", "id": "infinite_scroll"}).find_all("a")
# print(image_list)
Href_list = []
Alt_list = []
for href in image_list:
    href_url = "https://www.umei.cc"+href.get("href")
    try:
        title = href.find("img").get("alt")
        src = href.find("img").get("data-original")

    except AttributeError:
        pass
    else:
        alt = title
        print(f"{href_url},  {alt}\n {src}")
        Href_list.append(href_url)
        Alt_list.append(alt)

        child_page = requests.get(f"{href_url}")
        child_page.encoding = "utf-8"
        soup = BeautifulSoup(child_page.text, "html.parser")
        image_list = soup.find("a", attrs={"class": "noclick"})

        # print(image_list.text.split("/")[1])
        try:
            num = image_list.text.split("/")[1]
        except AttributeError:
            pass
            # print("This href_url can't found a element of 'image_list'")
        else:
            for i in range(2, int(num)+1):
                href = href_url
                url = href.split(".")
                print(url)
                new_url1 = url[0] + "."
                new_url2 = url[1] + "."
                new_url3 = url[2] + f"_{i}."
                url[2] = new_url3
                new_str = new_url1 + new_url2 + new_url3 + url[3]
                print(new_str)
print(Href_list)
print(Alt_list)

# 2013就有这样的Jk图片，她可正是走在了时代的前端昂，妥妥的一位潮妹
# 图片的第一张
