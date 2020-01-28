""" Module v1 """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)


app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def close_session(self):
    """ close_session
    """
    storage.close()


@app.errorhandler(404)
def error_404(self):
    """ handle 404 error
    """
    return jsonify({"error": "Not found"})

if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if host is None:
        host = '0.0.0.0'
    if port is None:
        port = '5000'
    app.run(host=host, port=port)
