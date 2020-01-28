""" Module States """
from flask import Flask, request, abort
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/states', methods = ['GET'], strict_slashes=False)
def all_states():
    """ all_states
        Return: all states
    """
    return jsonify([i.to_dict() for i in storage.all('State').values()])


@app_views.route('/states/<state_id>', strict_slashes=False)
def states_with_id(state_id):
    """ states_with_id
        Return: retrieve the state according to the id
    """
    if request.method == 'GET':
        result = storage.get('State', state_id)
        if result is None:
            abort(404)
        else:
            return jsonify(result.to_dict())
    # elif request.method == 'POST':
    # elif request.method == 'PUT':
    # elif request.method == 'DELETE':
