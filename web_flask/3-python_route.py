#!/usr/bin/python3
""" add another webpage """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ return a greeting """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ return HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ return c with user choice """
    s = 'C {}'.format(text)
    s = s.replace('_', ' ')
    return s

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    """ return python with user choice, and default """
    s = 'Python {}'.format(text)
    s = s.replace('_', ' ')
    return s


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
