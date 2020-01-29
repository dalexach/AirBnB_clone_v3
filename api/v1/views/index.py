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
    objects = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']
    for i in objects:
        result[i] = storage.count(i)

    return jsonify(result)
