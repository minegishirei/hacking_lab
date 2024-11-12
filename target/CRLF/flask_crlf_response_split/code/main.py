from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__)

app.secret_key = "FLAG{this_is_secret_key}"

@app.route("/")
def page():
    # ユーザーからの入力をエスケープする
    if not request.args.get('username'):
        return make_response("please set username get parameter.")
    user_input = request.args.get('username', 'default')
    response = make_response("Cookie has been set.")
    response.headers['Set-Cookie'] = f"username={user_input}"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)
