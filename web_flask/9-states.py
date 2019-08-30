#!/usr/bin/python3
""" use flask to list all states """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def clean_up(self):
    storage.close()


@app.route('/states', strict_slashes=False)
def list_states():
    """ list the states in the db """
    d = storage.all('State')
    return render_template('9-states.html', d=d, one_state=False)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """ list cities for state in the db """
    state = 0
    d = storage.all('State')
    state_id = 'State.' + id
    if state_id in d:
        state = d[state_id]
    return render_template('9-states.html', d=state, one_state=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
