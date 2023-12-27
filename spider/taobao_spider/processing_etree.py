from lxml import etree
from bs4 import BeautifulSoup
with open("resp.txt", "r") as f:
    information = f.read()
process_information = etree.HTML(information)
soup = BeautifulSoup(information, "lxml")
print("\n\n\n\n")
information2 = soup.find_all("script")
print(information2)

