#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the <text>"""
    txt = text.replace("_", " ")

    return "C " + txt


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def pythoniscool(text="is cool"):
    """display “Python ”, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/number/<int:n>", strict_slashes=False)
def isnmber(n):
    """if n is a number print it"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def ntmplate(n):
    """display HTML page if n an int"""
    return render_template("5-number.html", pn=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
