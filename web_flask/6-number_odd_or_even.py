#!/usr/bin/python3
""" flask module """
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ returns string """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ returns string """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ returns string """
    new_str = "C"
    route_words = text.split('_')
    for word in route_words:
        new_str += " " + word
    return (new_str)


@app.route("/python", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>")
def python(text):
    """ returns string """
    new_str = "Python"
    route_words = text.split('_')
    for word in route_words:
        new_str += " " + word
    return (new_str)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ returns string """
    return str(n) + " is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ returns template """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even_template(n):
    """ returns template """
    num_state = ''
    if n % 2 == 0:
        num_state = "even"
    else:
        num_state = "odd"
    return render_template("6-number_odd_or_even.html", n=n, state=num_state)


if __name__ == '__main__':
    """ runs app """
    app.run(host="0.0.0.0", port=5000, debug=True)
