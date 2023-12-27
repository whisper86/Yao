import requests

url = "https://www.moyublog.com/e/moyublog/authcode/AuthcodeidentifyCode.php"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39X-Requested-With: XMLHttpRequest ',

    "Referer": "https://www.moyublog.com/hdwallpapers/22286.html",
    "Cookie":
        "Hm_lvt_49c4b0ea69fee92a4371c846dbe445b6=1700126821; "
        "moyublog_v2020checkfeedbackkey=1700127686%2C99fc626f412b8865c6d12be625ee64bd%2CEmpireCMS; "
        "moyublog_v2020lastsearchtime=1700128017; moyublog_v2020returnurl=https%3A%2F%2Fwww.moyublog.com%2Fhdwallpapers"
        "%2F22286.html; moyublog_v2020wxreturnurl=https%3A%2F%2Fwww.moyublog.com%2Fhdwallpapers%2F22286.html; "
        "PHPSESSID=u1ouqavpqbl8nntfai99bbm9a9; Hm_lpvt_49c4b0ea69fee92a4371c846dbe445b6=1700129829",
    "Origin": "https://www.moyublog.com",
}
params = {
    "dialog-verfiy-code": "S9oE",
    "classid": 95,
    "id": 22286,
    "pass": "054c2a360008bcdd2387463c3b06ed92"
}

info = requests.post(url, params=params, headers=headers)

print(info.text)
