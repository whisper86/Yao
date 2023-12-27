# author: yao
# datetime: 11/26/2022
import requests
import os

os.mkdir('vedio')
url = "https://vdn6.vzuu.com/HD/870c23bc-c129-11eb-824c-7695fb17a227-t1-vfEJwZ6MXO.mp4?pkey" \
      "=AAXq5_eeqcmAAisqfqtfyiIGz5cOe3GEIvFqTI2h4TTaYCG3ggpBGL4GUDh5udYJB0TixnVLFzRzeXc5ZOGCsl6p&c=avc.0.0&f=mp4&pu" \
      "=da4bec50&bu=http-da4bec50&expiration=1669424660&v=ks6 "

resp = requests.get(url)

with open("vedio/视频1.mp4", mode='wb')as f:
    f.write(resp.content)

print("视频下载完成")