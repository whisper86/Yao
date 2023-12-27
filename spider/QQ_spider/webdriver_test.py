# author: yao
# datetime: 11/27/2022
import json
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opt = Options()
# opt.add_argument("__headless")
web = Chrome(executable_path="D:\软件（自2021年08月03日）\Google\Chrome\Application\chromedriver.exe", options=opt)

web.get('https://i.qq.com/')

# web.add_cookie({
#     "_qpsvr_localtk": "0.18154320542595426",
#     "pgv_pvid": "6684545848",
#     "pgv_info=ssid": "s6883299316",
#     "uin": "o3079593805",
#     "skey": "@0RpxEtUNP",
#     "Rk": "qPPFYKf0m3",
#     "ptcz": "21f7a87fe35ea26683a5d14ed4919c4110c2fe313bb4abe518b17bf74cec9ba2",
#     "p_uin": "o3079593805",
#     "pt4_token": "YDF4kyflqs67HaUogesGuM8Ba1VLgaySDQbamamqc14_",
#     "p_skey": "*0KgqgsGkEP-hmCL9hIILM4vo73pmxTnBxGyt2XQdNE_",
#     "Loading": "Yes",
#     "qz_screen": "1440x960",
#     " 3079593805_todaycount": "0",
#     "3079593805_totalcount": "706",
#     "QZ_FE_WEBP_SUPPORT": "1",
#     "cpu_performance_v8": "1"
# })
f = open("my_cookies.json", mode='r')
cookies = json.load(f)
for cookie in cookies:
    web.add_cookie({
        "domain": "user.qzone.qq.com",
        "name": cookie["name"],
        "path": "/",
        "secure": "false",
        "value": "0"
    })
time.sleep(3)
web.get("https://i.qq.com/")