from bs4 import BeautifulSoup
import requests

url = "https://user.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds3_html_more?uin=3079593805&scope=0" \
      "&view=1&daylist=&uinlist=&gid=&flag=1&filter=all&applist=all&refresh=0&aisortEndTime=0&aisortOffset=0" \
      "&getAisort=0&aisortBeginTime=0&pagenum=2&externparam=basetime=1664772415&pagenum=2&dayvalue=11&getadvlast=0" \
      "&hasgetadv=&lastentertime=1666597292&LastAdvPos=0&UnReadCount=0&UnReadSum=-1&LastIsADV=0&UpdatedFollowUins" \
      "=&UpdatedFollowCount=0&LastRecomBrandID=&TRKPreciList=&firstGetGroup=0&icServerTime=0&mixnocache=0&scene=0" \
      "&begintime=1664772415&count=10&dayspac=11&sidomain=qzonestyle.gtimg.cn&useutf8=1&outputhtmlfeed=1&rd=0" \
      ".6549768714089563&usertime=1666597287121&windowId=0.230925550357304&g_tk=1471629197&g_tk=1471629197 "

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/106.0.0.0 Safari/537.36"
          }

resp = requests.get(url)
resp.encoding = "utf-8"

print(resp.text)
