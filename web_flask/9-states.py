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


@app.route('/states', strict_slashes=False)
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


@app.route('/cities_by_states', strict_slashes=False)
def all_state_city():
    '''Get all state and cities.'''
    state_list = storage.all('State').values()
    '''
    Create an ordered list of tuples
    [(state.id, state.name, ordered_list[(city.id, city.name)])]
    '''
    state_tuple_list = []
    for state in state_list:
        city_tuple_list = []
        for city in state.cities:
            city_tuple = (city.id, city.name)
            city_tuple_list.append(city_tuple)
        state_tuple = (state.id, state.name, city_tuple_list)
        state_tuple_list.append(state_tuple)
    ordered_state_list = sorted(state_tuple_list, key=itemgetter(1))
    return render_template(
        '8-cities_by_states.html',
        ordered_state_list=ordered_state_list
    )


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    '''
    Display a state depending if the id is found else
    return not found.
    '''
    flag = 0
    state_name = ''
    city_list = []
    state_list = storage.all('State').values()
    for state in state_list:
        if state.id == id:
            state_name = state.name
            flag = 1
            for city in state.cities:
                city_tuple = (city.id, city.name)
                city_list.append(city_tuple)
    return render_template(
        '9-states.html',
        city_list=city_list,
        flag=flag,
        state=state_name
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
