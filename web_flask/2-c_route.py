#!/usr/bin/python3
"""
starts a web app using flask, listening on port 5000
"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hell0():
    """returns greeting when route is called"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb when route hbnb is called"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """displays url <text> on page"""
    return f"C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
