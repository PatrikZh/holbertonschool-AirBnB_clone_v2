#!/usr/bin/python3
""" python module """
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(self):
    """ teardown context """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ states list """
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    """ runs app """
    app.run(host="0.0.0.0", port=5000)
