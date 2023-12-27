from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.taobao.com"
cookie = {"miid": 49510181814580702,
          "cna": "WKQVHFB7C2oCAXJnHUo+Jhq9",
          "t":" 1ab91084899c1baf5218ed01db14f4ca",
          "lgc": "tb590164015376",
          "tracknick": "tb590164015376",
          "enc": "tkex+6zlGVe+S/D7+BPMp3tD+3ViQxMkFKGXJHx5cGZ7IGgRYRMXM8DqQTrBzkcdknwXI1CmZ"
                 "+Kxei8RBtrFCUG4CgGgyCVBwK8WY11D+lM= ",
          "thw": "cn",
          "cookie2": "1be40f25ed6fb8585df37c3d3f0a1237",
          "v": 0,
          "_samesite_flag_": "true",
          "sgcookie": "E100Gz032RRkoaLu09pZcjIMcgOdxSrVcXnh5lanJzzng4By8BMn8/VEDBEAG3v/NrE/sNbFxmeZJ6zxsda/AU6lBud5P"
                      "+WS87j6i67Q5syPmZs= ",
          "unb": 2214084434289,
          "uc3": "nk2=F5RAS6NspzF+fetrois=&lg2=URm48syIIVrSKA==&vt3=F8dCvjEe8ElrnawcaNg=&id2=UUpgQhD5L/1MPIK35w==",
          "cancelledSubSites": "empty",
          "existShop": "MTY3MTg3MTY2NQ==",
          "uc4": "id4=0@U2gqzcA5Py/oeLwFw9pYAGnLjjdW/zz8&nk4=0@FY4L52AaGQWU0zQxoZnMPM7kGbbEB+te7Q==",
          "_l_g_": "Ug==",
          "xlly_s": 1,
          "_tb_token_": "eb44ab50d53be",
          "mt": "ci=-1_0",
          "_m_h5_tk": "9bd29ee9f2969a743c0309bbdb4cfe73_1671975609492",
          " _m_h5_tk_enc": "db39ee53b5a17ae0d541e2eeac9beb45",
          "uc1": "pas=0&existShop=false&cookie16=VFC/uZ9az08KUQ56dCrZDlbNdA==&cart_m=0&cookie14=UoezTpuvTtWXTQ==",
          "isg": "BKurfjPgTFppk5A_Yy6DCRgYOsmVwL9C4oywuB0oh-pBvMsepZBPkkkeFvzShxc6",
          "l": "fBrJk7gVTAcm1QWyBOfaFurza77OSIRYYuPzaNbMi9fPOT5B5PQ5W6S9XA86C3GVF6qBR3Sy87EXBeYBcQAonxv92j"
               "-la_kmndLHR35..",
          "tfstk": "cL6fBJA0sNByrzwinEZz0sqR4BJOwBFW2PTRcrebAQTRLe10Gv8IoTRmod-9V"
          }
web = Chrome()

web.get(url)
time.sleep(2)
web.add_cookie(cookie)

web.find_element_by_xpath('//*[@id="q"]').send_keys("关东煮", Keys.ENTER)

time.sleep(3)

items = web.find_elements_by_class_name("items")
# input("扫码登陆后敲回车")
time.sleep(2)
for item in items:
    print(item)
