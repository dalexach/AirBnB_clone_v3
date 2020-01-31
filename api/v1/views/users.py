#!/usr/bin/python3
""" Module Users """
from flask import Flask, request, abort
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET', 'POST'], strict_slashes=False)
def all_users():
    """ all_users
        Return: all users
    """
    if request.method == 'GET':
        return jsonify([i.to_dict() for i in storage.all('User').values()])
    elif request.method == 'POST':
        if request.get_json() is None:
            abort(400, {'message': 'Not a JSON'})
        if "name" not in request.get_json().keys():
            abort(400, {'message': 'Missing name'})
        instance = User(**request.get_json())
        instance.save()
        return jsonify(instance.to_dict()), 201


@app_views.route('/users/<user_id>',
                 methods=['GET', 'DELETE', 'PUT', 'POST'],
                 strict_slashes=False)
def users_with_id(user_id):
    """ users_with_id
        Return: retrieve the user according to the id
    """
    list_users = storage.all('User')
    if "User.{}".format(user_id) not in list_users:
        abort(404)
    if request.method == 'GET':
        result = storage.get('User', user_id)
        if result is None:
            abort(404)
        else:
            return jsonify(result.to_dict())
    elif request.method == 'DELETE':
        storage.delete(list_users["User.{}".format(user_id)])
        storage.save()
        return jsonify({})
    elif request.method == 'PUT':
        if request.get_json() is None:
            abort(400, {'message': 'Not a JSON'})

        user = storage.get('User', user_id)
        for key, value in request.get_json().items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(user, key, value)
        return jsonify(user.to_dict())
