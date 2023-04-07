#!/usr/bin/python3
""" Writing a script that starts a Flask web application"""
from flask import Flask
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


@app.route('/number/<n:n>', strict_slashes=False)
def number_int(n):
    ''' Adding only if number'''
    modified_text = ""
    for i in range(len(n)):
        if type(text[i]) == int:
            modified_text += text[i]
            print("n is a number")
        else:
            pass
    return modified_text 

if __name__ == '__main__':
    ''' Checking if main file'''
    app.run(host="0.0.0.0", port=5000, debug=True)
