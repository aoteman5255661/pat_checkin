import requests
import os
url = "https://pintia.cn/api/users/checkin"

headers = {
  'accept-language': 'zh-CN',
  'cookie': 'PTASession={}'.format(os.getenv('PTASession')),
}

response = requests.request("POST", url, headers=headers).json()

print(response)
print(response['error']['message'])

token = os.getenv('pushplus_token')
if not token:
  print("没有设置pushplus_token返回")
url = "http://www.pushplus.plus/send?token={}&content={}".format(token, response)
response1 = requests.request("POST", url)
print(response1.text)
