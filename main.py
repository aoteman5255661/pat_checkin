import requests
import os
url = "https://pintia.cn/api/users/checkin"

headers = {
  'accept-language': 'zh-CN',
  'cookie': 'PTASession={}'.format(os.getenv('PTASession')),
}

response = requests.request("POST", url, headers=headers)

print(response.text)
