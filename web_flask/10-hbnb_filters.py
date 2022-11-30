#!/usr/bin/python3
'''
This script returns the list of states in the database.
'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    '''Close storage connect when the session is popped.'''
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''Renders template showing states, cities and amenities.'''
    state_dict = storage.all('State')
    amenity_dict = storage.all('Amenity')
    return render_template(
        '10-hbnb_filters.html',
        states=state_dict,
        amenities=amenity_dict
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
