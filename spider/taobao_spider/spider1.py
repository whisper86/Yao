import requests
from lxml import etree

url = "https://cart.taobao.com/cart.htm?spm=a21bo.jianhua.0.0.5af911d9damEI5"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36",
    "Cookie": "miid=49510181814580702; cna=WKQVHFB7C2oCAXJnHUo+Jhq9; t=1ab91084899c1baf5218ed01db14f4ca; "
              "lgc=tb5901640153 "
              "76; tracknick=tb590164015376; "
              "enc=tkex+6zlGVe+S/D7+BPMp3tD+3ViQxMkFKGXJHx5cGZ7IGgRYRMXM8DqQTrBzkcdknwXI1CmZ"
              "+Kxei8RBtrFCUG4CgGgyCVBwK8WY11D+lM=; ubn=p; thw=cn; ucn=center; "
              "cookie2=1be40f25ed6fb8585df37c3d3f0a1237; _tb_token_=7e34383de7bee; v=0; _samesite_flag_=true; "
              "_m_h5_tk=da2a03ef0bdc8b8be12eec5451a9b18a_1671879552732; "
              "_m_h5_tk_enc=dfd772faa3aa1a95970260d2b8e1ad58; xlly_s=1; "
              "sgcookie=E100Gz032RRkoaLu09pZcjIMcgOdxSrVcXnh5lanJzzng4By8BMn8/VEDBEAG3v/NrE/sNbFxmeZJ6zxsda/AU6lBud5P"
              "+WS87j6i67Q5syPmZs=; unb=2214084434289; "
              "uc3=nk2=F5RAS6NspzF+fetrois=&lg2=URm48syIIVrSKA==&vt3=F8dCvjEe8ElrnawcaNg=&id2=UUpgQhD5L/1MPIK35w==; "
              "csg=c56cf1b1; cancelledSubSites=empty; cookie17=UUpgQhD5L/1MPIK35w==; dnk=tb590164015376; "
              "skt=2e38e8c9aa5ff3e2; existShop=MTY3MTg3MTY2NQ==; "
              "uc4=id4=0@U2gqzcA5Py/oeLwFw9pYAGnLjjdW/zz8&nk4=0@FY4L52AaGQWU0zQxoZnMPM7kGbbEB+te7Q==; "
              "_cc_=VT5L2FSpdA==; _l_g_=Ug==; sg=69f; _nk_=tb590164015376; "
              "cookie1=UoDfwceE6qkJMYFRMaQkDeNbHPdXTGt1ASwBN3HdVWI=; mt=ci=70_1; "
              "isg=BK-vcnCUEIAxABSD3xrP3Ty0PsW5VAN2RvA0JME8S54lEM8SySSTxq3ClgAuc9vu; "
              "tfstk=cyMcBWDSwz_CRWJtPqwXpAZbL9vdwiL4umoZU3lxx6-hN_C0r_5EeIp3yeTV1; "
              "l=fBrJk7gVTAcm1_BsBOfaFurza77OSIRYYuPzaNbMi9fPOQfB5pcAW6SrQ8T6C3GVF6JHR3Sy87EXBeYBc3xonxvOUKaOYMkmndLHR"
              "35..; uc1=pas=0&cookie14=UoezTpqOgURxcA==&existShop=false&cookie15=UIHiLt3xD8xYTw==&cookie16=WqG3DMC9UpA"
              "PBHGz5QBErFxlCA==&cookie21=VFC/uZ9ainBZ&cart_m=0 "
}

resp = requests.get(url, headers=headers)
resp.encoding = "gbk"
print(resp.text)
processing_html = etree.HTML(resp.text)
print(processing_html)