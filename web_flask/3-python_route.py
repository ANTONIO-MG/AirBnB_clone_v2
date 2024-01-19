#!/usr/bin/python3
""" Starts a Flash Web Application """
# script that starts a Flask web application:
# web application listening on 0.0.0.0, port 5000
# Routes:  "/"" display “Hello HBNB!”
# /hbnb: display “HBNB”
# python/<text>: display “Python ”, followed by the value of the text
# (replace underscore _ symbols with a space )
# The default value of text is “is cool”
# option strict_slashes=False in route definition

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ returns a message on the index """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_world2():
    """ returns a message on the hbnb extension """
    return "HBN"


@app.route('/c/<text>', strict_slashes=False)
def hello_world3(text):
    """ returns a message based on the txt passed as arg """
    input = escape(text)
    new_text = input.replace('_', ' ')
    return f"C {escape(new_text)}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_world5(text='is cool'):
    """ returns a message based on teh text passed or teh default message """
    input = escape(text)
    new_text = input.replace('_', ' ')
    return f"Python {escape(new_text)}"


@app.route('/hbnb', strict_slashes=False)
def hello_world4():
    """ returns a message on the hbnb extension """
    return "HBNB"


if __name__ == "__main__":
    """ if not imported execute the main function """
    app.run(host='0.0.0.0', port=5000)
