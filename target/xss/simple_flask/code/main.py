from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XSS Demo</title>
</head>
<body>
    <h1>XSS Vulnerability Test</h1>
    <form action="#" method="GET">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name">
        <button type="submit">Submit</button>
    </form>

    <p>Hello! <span id="output"></span></p>

    <script>
        // URLクエリパラメータを取得
        const params = new URLSearchParams(window.location.search);
        const userInput = params.get('name');
        if (userInput) {
            // 悪意のあるスクリプトが動くよう innerHTML を利用
            document.getElementById('output').innerHTML = userInput;
        }
    </script>
</body>
</html>

  """

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)