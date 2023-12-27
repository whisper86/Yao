import requests
import json

url = "https://www.pearvideo.com/video_1728939"
contID = url.split("_")[1]
heads = {
    "Cookie": 'aliyungf_tc=6669e67c5361e4b14605431cf6743c1bf299f903843d6f3d8ea45d42b4943b16; acw_tc=76b20f8816701266783617908e56f0beb6e36c528d4229f164848b0b30cccd; JSESSIONID=83C4A5CFB5D2EEA2F6CB8FED41AD86FB; PEAR_UUID=516dca37-9efc-4220-8459-a21ad9aa17ac; _uab_collina=167012667607412086659097; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1670126676; p_h5_u=0BF505C1-6905-45D4-8F6D-F81D491FECC8; PEAR_UID="LoJ/02qb7W0VYBIVXVnotg=="; PEAR_TOKEN=8c643307-bde5-48e3-8fac-732e06f6cbc3; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1670126942; SERVERID=ed8d5ad7d9b044d0dd5993c7c771ef48|1670126954|1670126678',
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36 ",
    "Referer": f"{url}"
}

videoStatus = "https://www.pearvideo.com/videoStatus.jsp?contId=1728939&mrd=0.5566473962488372"

resp = requests.get(videoStatus, headers=heads)
response = resp.text
dic = json.loads(response)

# print(dic)

# mp4_Url = https://video.pearvideo.com/mp4/adshort/20210509/cont-1728939-15671843_adpkg-ad_hd.mp4
# srcUrl = https://video.pearvideo.com/mp4/adshort/20210509/1670127444365-15671843_adpkg-ad_hd.mp4
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]

video_url = srcUrl.replace(systemTime, f"cont-{contID}")
print(video_url)

with open("video.mp4", mode="wb") as f:
    f.write(requests.get(video_url).content)
