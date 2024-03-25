#!/usr/bin/python3
"""start Flask my web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """printsHello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returning HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """displays “C ” followed by the <text>"""
    txt = text.replace("_", " ")

    return "C " + txt


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
