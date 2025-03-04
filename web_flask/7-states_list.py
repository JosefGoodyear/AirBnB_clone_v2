#!/usr/bin/python3
""" use flask to list all states """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def clean_up(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ list the states in the db """
    d = storage.all(State)
    return render_template('7-states_list.html', d=d)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
