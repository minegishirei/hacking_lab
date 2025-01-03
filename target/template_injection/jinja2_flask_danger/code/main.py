from flask import Flask, request
from jinja2 import Environment

app = Flask(__name__)
Jinja2 = Environment()

app.secret_key = "FLAG{this_is_secret_key}"

@app.route("/")
def page():
    if not request.values.get('name'):
        return "Hello"
    name = request.values.get('name')
    
    # SSTI VULNERABILITY
    # The vulnerability is introduced concatenating the
    # user-provided `name` variable to the template string.
    output = Jinja2.from_string('Hello ' + name + '!').render()
    
    # Instead, the variable should be passed to the template context.
    # Jinja2.from_string('Hello {{name}}!').render(name = name)

    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)
