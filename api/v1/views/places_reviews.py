#!/usr/bin/python3
""" Module Cities """
from flask import Flask, request, abort
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.place import Place
from models.review import Review


@app_views.route('/places/<place_id>/reviews',
                 methods=['GET', 'POST'],
                 strict_slashes=False)
def all_reviews(place_id):
    """ all_reviews
        Return: all reviews
    """
    list_places = storage.all('Place')
    if "Place.{}".format(place_id) not in list_places:
        abort(404)
    if request.method == 'GET':
        return jsonify([i.to_dict() for i in
                       storage.get('Place', place_id).reviews])
    elif request.method == 'POST':
        if request.get_json() is None:
            abort(400, 'Not a JSON')
        if "name" not in request.get_json().keys():
            abort(400, 'Missing name')
        final_dict = request.get_json()
        final_dict.update({'place_id': place_id})
        instance = Review(**final_dict)
        instance.save()
        return jsonify(instance.to_dict()), 201


@app_views.route('/reviews/<review_id>',
                 methods=['GET', 'DELETE', 'PUT', 'POST'],
                 strict_slashes=False)
def reviews_with_id(review_id):
    """ reviews_with_id
        Return: retrieve the review according to the id
    """
    list_reviews = storage.all('Review')
    if "Review.{}".format(review_id) not in list_reviews:
        abort(404)
    if request.method == 'GET':
        result = storage.get('Review', review_id)
        if result is None:
            abort(404)
        else:
            return jsonify(result.to_dict())
    elif request.method == 'DELETE':
        storage.delete(list_reviews["Review.{}".format(review_id)])
        storage.save()
        return jsonify({})
    elif request.method == 'PUT':
        if request.get_json() is None:
            abort(400, 'Not a JSON')

        review = storage.get('Review', review_id)
        for key, value in request.get_json().items():
            if key in ['id', 'created_at', 'updated_at']:
                pass
            else:
                setattr(review, key, value)
        return jsonify(review.to_dict())
