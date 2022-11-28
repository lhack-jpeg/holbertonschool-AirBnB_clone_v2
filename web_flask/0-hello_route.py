#!/usr/bin/python3
'''
Script for very basic web application. Returns the string
requested by any device on the network.
'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
