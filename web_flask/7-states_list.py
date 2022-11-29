#!/usr/bin/python3
'''
This script returns the list of states in the database.
'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db():
    '''Close storage connect when the session is popped.'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def all_state_list():
    '''Gets all states in the area.'''
    state_list = storage.all('State').value()
    print(state_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
