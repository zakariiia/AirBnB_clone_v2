#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """returning Hello HBNB!"""
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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def pythoniscool(text="is cool"):
    """displays “Python ”, followed by the value of the text variable"""
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


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page if n is an int"""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", pn=n,
                               evenness="even")
    else:
        return render_template("6-number_odd_or_even.html", pn=n,
                               evenness="odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
