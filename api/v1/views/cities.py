""" Module Cities """
from flask import Flask, request, abort
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<state_id>/cities',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def all_cities(state_id):
    """ all_cities
        Return: all cities
    """
    list_states = storage.all('State')
    if "State.{}".format(state_id) not in list_states:
        abort(404)
    if request.method == 'GET':
        return jsonify([i.to_dict() for i in
                       storage.get('State', state_id).cities])
    elif request.method == 'POST':
        if request.content_type != 'application/json':
            abort(400, {'message': 'Not a JSON'})
        if "name" not in request.get_json().keys():
            abort(400, {'message': 'Missing name'})
        final_dict = request.get_json()
        final_dict.update({'state_id': state_id})
        instance = City(**final_dict)
        instance.save()
        return jsonify(instance.to_dict()), 201


@app_views.route('/cities/<city_id>',
                 methods=['GET', 'DELETE', 'PUT', 'POST'],
                 strict_slashes=False)
def cities_with_id(city_id):
    """ cities_with_id
        Return: retrieve the city according to the id
    """
    list_cities = storage.all('City')
    if "City.{}".format(city_id) not in list_cities:
        abort(404)
    if request.method == 'GET':
        result = storage.get('City', city_id)
        if result is None:
            abort(404)
        else:
            return jsonify(result.to_dict())
    elif request.method == 'DELETE':
        storage.delete(list_cities["City.{}".format(city_id)])
        storage.save()
        return jsonify({})
    elif request.method == 'PUT':
        if request.content_type != 'application/json':
            abort(400, {'message': 'Not a JSON'})

        city = storage.get('City', city_id)
        for key, value in request.get_json().items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(city, key, value)
        return jsonify(city.to_dict())
