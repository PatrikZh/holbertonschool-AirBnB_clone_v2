#!/usr/bin/python3
""" Writing a script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' Returns string'''
    return "Hello HBNB!"
