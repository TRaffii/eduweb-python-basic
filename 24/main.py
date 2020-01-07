from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "@@@@Hello, World@@@@"


@app.route("/greetings/")
@app.route("/greetings/<username>")
def greetings(username="User"):
    greetings = "Hi " + username
    return greetings


@app.route("/greetings/<name>/<surname>")
def full_greeting(name, surname):
    return f"Welcome {name.capitalize()} {surname.capitalize()}"


@app.route('/login', methods=['POST'])
def login():
    if request.form['name'] == "Admin" and request.form['password'] == "123":
        return "Success!"
    return "Failure"


if __name__ == '__main__':
    app.run(debug=True)
