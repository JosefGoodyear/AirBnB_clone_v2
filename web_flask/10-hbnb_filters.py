#!/usr/bin/python3
""" use flask to list all states """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def clean_up(self):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ hbnb filters """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
