from flask import Flask, request
from lxml import etree  # lxmlを使用

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse_xml():
    # クライアントから受信したXMLデータ
    xml_data = request.data.decode('utf-8')
    print(f"Received XML:\n{xml_data}")

    # lxmlのパーサー設定
    parser = etree.XMLParser(load_dtd=True, resolve_entities=True)

    try:
        # XMLデータを解析
        root = etree.fromstring(xml_data, parser=parser)

        # XML要素からデータを抽出
        to = root.findtext('to')
        from_ = root.findtext('from')  # Pythonの予約語 'from' を避けて 'from_' を使用
        heading = root.findtext('heading')
        body = root.findtext('body')

        # メール本文を作成
        email_body = f"""
To: {to}
From: {from_}
Subject: {heading}

{body}
        """
        return f"Generated Email Body:\n{email_body.strip()}"
    except Exception as e:
        return f"Error parsing XML: {str(e)}", 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)