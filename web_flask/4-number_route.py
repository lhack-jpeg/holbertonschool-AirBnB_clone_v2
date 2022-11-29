#!/usr/bin/python3
"""
Script for very basic web application. Returns the string
requested by any device on the network depending on the phrases
after the slash.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Returns the string below"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def school():
    """Returns the string below"""
    return "HBNB"


@app.route('/c/<text>')
def c_is(text):
    ''' returns the string "C <text>".'''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is(text):
    '''Returns the string "python is..." defaults to is cool.'''
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>")
def is_n_number(n):
    """Prints out n is number if n is type int."""
    if isinstance(n, int):
        return str(n) + ' is a number'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
