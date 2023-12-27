import requests

session = requests.session()

url = "https://www.moyublog.com/e/moyublog/HD_Wallpapers/get.php?classid=95&id=5481&pass" \
      "=3d70e6e90085a270b858ca12a6191ddc "

header = {
    "dialog-verfiy-code":"S9oE",
    "cookie": "Hm_lvt_49c4b0ea69fee92a4371c846dbe445b6=1700121523; PHPSESSID=lnkafo75t6lf2k0l8cag3r92pm; "
              "moyublog_v2020lastsearchtime=1700125604; "
              "moyublog_v2020moyublog_v2020=b860d7ad7095f83fd51b615d94e4f361; moyublog_v2020qdelinfo=dgcms; "
              "moyublog_v2020mlusername=Whisper_Y; moyublog_v2020mluserid=141267; moyublog_v2020mlgroupid=1; "
              "moyublog_v2020mlrnd=v4kEr5IdwIzUYoQVYmy9; moyublog_v2020mlauth=7c42c21f9830812c83d9798a9b6d5fb4; "
              "moyublog_v2020returnurl=https%3A%2F%2Fwww.moyublog.com%2Fhdwallpapers%2F5481.html; "
              "moyublog_v2020wxreturnurl=https%3A%2F%2Fwww.moyublog.com%2Fhdwallpapers%2F5481.html; "
              "Hm_lpvt_49c4b0ea69fee92a4371c846dbe445b6=1700131619 "
    }
image = session.get(url, headers=header)

# with open("image2.text", 'wb') as f:
#     f.write(image.content)
#     print(image.content)
#     print("All is done")
print(image.text)

session.close()
