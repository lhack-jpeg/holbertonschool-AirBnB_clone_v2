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
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def school():
    return 'HBNB'


@app.route('/c/<text>')
def c_is(text):
    ''' returns the string "C <text>".''''
    return f'C {text}'.replace('_', " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
