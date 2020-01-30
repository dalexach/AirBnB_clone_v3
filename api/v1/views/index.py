#!/usr/bin/python3
""" Module index """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """ status:
        return the status
    """
    return jsonify({'status': "OK"})


@app_views.route('/stats')
def stats():
    """ stats:
        return the number of each object
    """
    result = {}
    objects = {'amenities': 'Amenity', 'cities': 'City',
               'places': 'Place', 'reviews': 'Review',
               'states': 'State', 'users': 'User'}
    for key, value in objects.items():
        result[key] = storage.count(value)

    return jsonify(result)
