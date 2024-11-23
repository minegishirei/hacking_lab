from flask import Flask, request, render_template_string, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "super_secret_key"  # セッションの暗号化に必要
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# ダミーのデータベース
user_data = {"user1": "password123"}
user_balances = {"user1": 1000}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in user_data and user_data[username] == password:
            session["username"] = username
            return redirect(url_for("dashboard"))
        return "ログイン失敗", 401
    return '''
        <h1>ログイン</h1>
        <form method="POST">
            <label>ユーザー名:</label>
            <input type="text" name="username" required>
            <br>
            <label>パスワード:</label>
            <input type="password" name="password" required>
            <br>
            <button type="submit">ログイン</button>
        </form>
    '''

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))
    username = session["username"]
    return f'''
        <h1>ダッシュボード</h1>
        <p>こんにちは、{username}さん！</p>
        <p>残高: {user_balances[username]}円</p>
        <a href="/transfer">送金ページへ</a>
    '''

@app.route("/transfer", methods=["GET", "POST"])
def transfer():
    if "username" not in session:
        return redirect(url_for("login"))
    username = session["username"]
    if request.method == "POST":
        amount = int(request.form.get("amount"))
        user_balances[username] -= amount
        return redirect(url_for("dashboard"))
    return '''
        <h1>送金ページ</h1>
        <form method="POST">
            <label>送金額: </label>
            <input type="number" name="amount" required>
            <br>
            <button type="submit">送金</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)