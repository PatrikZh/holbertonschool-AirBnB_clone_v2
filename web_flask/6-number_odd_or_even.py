#!/usr/bin/python3
""" Writing a script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' Returns string'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Returns string'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    ''' Displaying modified string'''
    value = "C"
    modified_text = ""
    for i in range(len(text)):
        if text[i] == "_":
            modified_text += " "
        else:
            modified_text += text[i]
    return value + " " + modified_text


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def modify_text(text):
    ''' Displaying modified string'''
    value = "Python"
    modified_text = ""
    for i in range(len(text)):
        if text[i] == "_":
            modified_text += " "
        else:
            modified_text += text[i]
    return value + " " + modified_text


@app.route('/number/<int:n>', strict_slashes=False)
def number_int(n):
    ''' Adding only if number'''
    modified_int = str(n)
    message = "{} is a number".format(modified_int)
    return message


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' HTML comes in only if n is an integer'''
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    ''' Checking number n is even or odd if its integer'''
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == '__main__':
    ''' Checking if main file'''
    app.run(host="0.0.0.0", port=5000, debug=True)
