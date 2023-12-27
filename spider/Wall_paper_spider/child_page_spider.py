import requests
from bs4 import BeautifulSoup

headers = {
    "User_Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Mobile Safari/537.36 "
}

for i in range(1, 21):
    url = f"https://www.macw.com/dlist/9_1_{i}.html"
    child_page_resp = requests.get(url, headers=headers)

    soup = BeautifulSoup(child_page_resp.text, "lxml")
    main_Find = soup.find("ul", attrs={"class": "wallpaper-static clearfix"}).find_all("li")
    for li in main_Find:
        img = li.find("div", attrs={"class": "img"}).find("img")
        title = img.get("alt")
        src = img.get("src")
        alt = f"{title}" + "." + src.split(".")[-1]
        try:
            with open(f"最新静态壁纸/{alt}", mode="wb") as f:
                f.write(requests.get(src).content)
                print(f"{alt}爬取完成")
        except FileNotFoundError:
            print(f"{alt}\n")
            print(f"{src}")
        else:
            pass
    print(f"已经爬取了{i}页")
    x = input("按下回车以爬取下一页\n")
    print("开始爬取下一页")

