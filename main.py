import requests
import sys
import os
import time
url = "https://pintia.cn/api/users/checkin"

headers = {
  'accept-language': 'zh-CN',
  'cookie': 'PTASession={}'.format(os.getenv('PTASession')),
}

response = requests.request("POST", url, headers=headers).json()

print(response)
print(response['error']['message'])
response['time'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(1594368331))
token = os.getenv('pushplus_token')
if not token:
  print("没有设置pushplus_token返回")
  sys.exit()
url = "http://www.pushplus.plus/send?token={}&content={}".format(token, response)
response1 = requests.request("POST", url)
print(response1.text)
