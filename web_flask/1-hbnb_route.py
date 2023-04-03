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


if __name__ == '__main__':
    """ runs app """
    app.run(host="0.0.0.0", port=5000, debug=True)
