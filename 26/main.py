from flask import Flask, request, render_template

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


@app.route('/login_form')
def login_form():
    return render_template('layout_form.html', default_username="Provide username")

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
