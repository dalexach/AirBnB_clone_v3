#!/usr/bin/python3
""" Module States """
from flask import Flask, request, abort
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def all_states():
    """ all_states
        Return: all states
    """
    if request.method == 'GET':
        return jsonify([i.to_dict() for i in storage.all('State').values()])
    elif request.method == 'POST':
        if request.get_json() is None:
            abort(400, {'message': 'Not a JSON'})
        if "name" not in request.get_json().keys():
            abort(400, {'message': 'Missing name'})
        instance = State(**request.get_json())
        instance.save()
        return jsonify(instance.to_dict()), 201


@app_views.route('/states/<state_id>',
                 methods=['GET', 'DELETE', 'PUT', 'POST'],
                 strict_slashes=False)
def states_with_id(state_id):
    """ states_with_id
        Return: retrieve the state according to the id
    """
    list_states = storage.all('State')
    if "State.{}".format(state_id) not in list_states:
        abort(404)
    if request.method == 'GET':
        result = storage.get('State', state_id)
        if result is None:
            abort(404)
        else:
            return jsonify(result.to_dict())
    elif request.method == 'DELETE':
        storage.delete(list_states["State.{}".format(state_id)])
        storage.save()
        return jsonify({})
    elif request.method == 'PUT':
        if request.get_json() is None:
            abort(400, {'message': 'Not a JSON'})

        state = storage.get('State', state_id)
        for key, value in request.get_json().items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(state, key, value)
        return jsonify(state.to_dict())
