import requests
import os
url = "https://pintia.cn/api/users/checkin"

payload = "{}"
headers = {
  # 'authority': 'pintia.cn',
  # 'pragma': 'no-cache',
  # 'cache-control': 'no-cache',
  # 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
  # 'dnt': '1',
  'accept-language': 'zh-CN',
  # 'sec-ch-ua-mobile': '?0',
  # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.0.0 Safari/537.36',
  # 'content-type': 'application/json;charset=UTF-8',
  # 'accept': 'application/json;charset=UTF-8',
  # 'x-marshmallow': '',
  # 'x-lollipop': 'eeec4fd8bb9f04fadb578399aa05b6cb',
  # 'sec-ch-ua-platform': '"Windows"',
  # 'origin': 'https://pintia.cn',
  # 'sec-fetch-site': 'same-origin',
  # 'sec-fetch-mode': 'cors',
  # 'sec-fetch-dest': 'empty',
  # 'referer': 'https://pintia.cn/market',
  # 'cookie': 'PTASession=58f96fbe-d2b8-472f-a550-4e6dde61f4de',
  'cookie': os.getenv('pat_cookie')
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
