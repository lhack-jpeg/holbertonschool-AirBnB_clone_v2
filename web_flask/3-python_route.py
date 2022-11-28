#!/usr/bin/python3
'''
Script for very basic web application. Returns the string
requested by any device on the network depending on the phrases
after the slash.
'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    '''Returns the string below'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def school():
    '''Returns the string below'''
    return 'HBNB'


@app.route('/c/<text>')
def c_is(text):
    ''' returns the string "C <text>".'''
    return f'C {text}'.replace('_', " ")


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is(text):
    '''Returns the string "python is..." defaults to is cool.'''
    return f'Python {text}'.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
