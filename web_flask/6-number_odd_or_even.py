#!/usr/bin/python3
""" add another webpage """
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ print number if it's an int """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ make html from a template """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ make html from a template. return odd or even """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
