from bs4 import BeautifulSoup

with open("倪小璐's academic performance.html", mode="r", encoding="utf-8") as f:
    html = f.read()

    soup = BeautifulSoup(html, "html.parser")

    print(soup)