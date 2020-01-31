#!/usr/bin/python3
""" Module States """
from flask import Flask, request, abort
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET', 'POST'], strict_slashes=False)
def all_amenities():
    """ all_amenities
        Return: all amenities
    """
    if request.method == 'GET':
        return jsonify([i.to_dict() for i in storage.all('Amenity').values()])
    elif request.method == 'POST':
        if request.content_type != 'application/json':
            abort(400, {'message': 'Not a JSON'})
        if "name" not in request.get_json().keys():
            abort(400, {'message': 'Missing name'})
        instance = Amenity(**request.get_json())
        instance.save()
        return jsonify(instance.to_dict()), 201


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET', 'DELETE', 'PUT', 'POST'],
                 strict_slashes=False)
def aminities_with_id(amenity_id):
    """ amenities_with_id
        Return: retrieve the amenity according to the id
    """
    list_ameinities = storage.all('Amenity')
    if "Amenity.{}".format(amenity_id) not in list_amenities:
        abort(404)
    if request.method == 'GET':
        result = storage.get('Amenity', amenity_id)
        if result is None:
            abort(404)
        else:
            return jsonify(result.to_dict())
    elif request.method == 'DELETE':
        storage.delete(list_states["Amenity.{}".format(amenity_id)])
        storage.save()
        return jsonify({})
    elif request.method == 'PUT':
        if request.content_type != 'application/json':
            abort(400, {'message': 'Not a JSON'})

        amenity = storage.get('Amenity', amenity_id)
        for key, value in request.get_json().items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(amenity, key, value)
        return jsonify(amenity.to_dict())
