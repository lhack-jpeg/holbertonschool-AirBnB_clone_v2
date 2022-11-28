#!/usr/bin/python3
"""starts a flask web app listenning on port 5000"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns a greeting when route is queried"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb for /hbnb query"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """displays url text on page"""
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
