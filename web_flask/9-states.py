#!/usr/bin/python3
"""Flask app with data from list of dictionaries"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def state_list():
    """ Route for states path"""
    states = storage.all("State").values()
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_city_list(id):
    """ Route for states path in terms of id"""
    state = None
    states = storage.all("State").values()
    for element in states:
        if element.id == id:
            state = element
    return render_template('9-states.html',
                           state=state)


@ app.teardown_appcontext
def close_storage(self):
    storage.close()


if __name__ == '__main__':
    """ Making it an main program"""
    app.run(host='0.0.0.0', port=5000)
