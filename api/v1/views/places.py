#!/usr/bin/python3
""" Module Cities """
from flask import Flask, request, abort
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.city import City
from models.place import Place


@app_views.route('/cities/<city_id>/places',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def all_places(city_id):
    """ all_places
        Return: all places
    """
    list_cities = storage.all('City')
    if "City.{}".format(city_id) not in list_cities:
        abort(404)
    if request.method == 'GET':
        return jsonify([i.to_dict() for i in
                       storage.get('City', city_id).places])
    elif request.method == 'POST':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        if "name" not in request.get_json().keys():
            abort(400, 'Missing name')
        final_dict = request.get_json()
        final_dict.update({'city_id': city_id})
        instance = Place(**final_dict)
        instance.save()
        return jsonify(instance.to_dict()), 201


@app_views.route('/places/<place_id>',
                 methods=['GET', 'DELETE', 'PUT', 'POST'],
                 strict_slashes=False)
def places_with_id(place_id):
    """ places_with_id
        Return: retrieve the place according to the id
    """
    list_places = storage.all('Place')
    if "Place.{}".format(place_id) not in list_places:
        abort(404)
    if request.method == 'GET':
        result = storage.get('Place', place_id)
        if result is None:
            abort(404)
        else:
            return jsonify(result.to_dict())
    elif request.method == 'DELETE':
        storage.delete(list_places["Place.{}".format(place_id)])
        storage.save()
        return jsonify({})
    elif request.method == 'PUT':
        if request.get_json() is None:
            abort(400, 'Not a JSON')

        place = storage.get('Place', place_id)
        for key, value in request.get_json().items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(place, key, value)
        return jsonify(place.to_dict())
