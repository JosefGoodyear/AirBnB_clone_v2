#!/usr/bin/python3
""" use flask to list all states """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def clean_up(self):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_states():
    """ list the states in the db """
    d = storage.all('State')
    return render_template('8-cities_by_states.html', d=d)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
