#!/usr/bin/python3
"""
Script for very basic web application. Returns the string
requested by any device on the network depending on the phrases
after the slash.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Returns the string below"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def school():
    """Returns the string below"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    ''' returns the string "C <text>".'''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>')
def python_is(text):
    '''Returns the string "python is..." defaults to is cool.'''
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def is_n_number(n):
    """Prints out n is number if n is type int."""
    if isinstance(n, int):
        return str(n) + ' is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_template(n):
    """
    Returns a template of a html document if n is
    an integer.
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def n_odd_even(n):
    '''
    Display Html page if n is integer.
    H1 tag: N is even | odd.
    '''
    if isinstance(n, int):
        return render_template(
            '6-number_odd_or_even.html',
            n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
