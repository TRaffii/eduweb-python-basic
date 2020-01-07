from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    raise ValueError
    return "@@@@Hello, World@@@@"


@app.route("/greetings/")
@app.route("/greetings/<username>")
def greetings(username="User"):
    greetings = "Hi " + username
    return greetings


@app.route("/greetings/<name>/<surname>")
def full_greeting(name, surname):
    return f"Welcome {name.capitalize()} {surname.capitalize()}"


if __name__ == '__main__':
    app.run(debug=True)
