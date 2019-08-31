#!/usr/bin/python3
""" use flask to list all states """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def clean_up(self):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ hbnb filters """
    return render_template('10-hbnb_filters.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
