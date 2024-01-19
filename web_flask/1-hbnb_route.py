#!/usr/bin/python3
""" Starts a Flash Web Application """
# script that starts a Flask web application:
# web application listening on 0.0.0.0, port 5000
# Routes:  "/"" display “Hello HBNB!”
# /hbnb: display “HBNB”
# option strict_slashes=False in route definition

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ returns a message on the index """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_world2():
    """ returns a message on the hbnb extension """
    return "HBNB"


if __name__ == "__main__":
    """ if not imported execute the main function """
    app.run(host='0.0.0.0', port=5000)
