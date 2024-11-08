import random
from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def index():
    query = 3
    if request.method == 'GET':
        query = request.args.get('query', '')
    return render_template("index.html", query = query)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)