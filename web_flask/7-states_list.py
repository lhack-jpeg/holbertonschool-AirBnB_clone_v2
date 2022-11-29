#!/usr/bin/python3
'''
This script returns the list of states in the database.
'''
from flask import Flask, render_template
from models import storage
from operator import itemgetter

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    '''Close storage connect when the session is popped.'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def all_state_list():
    '''Gets all states in the area.'''
    state_list = storage.all('State').values()
    state_tuple_list = []
    for state in state_list:
        state_tuple = (state.id, state.name)
        state_tuple_list.append(state_tuple)
    # sorts array of tuples by the name value.
    ordered_state_list = sorted(state_tuple_list, key=itemgetter(1))
    return render_template(
        '7-states_list.html',
        ordered_state_list=ordered_state_list
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
