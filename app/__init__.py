from flask import Flask, jsonify


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "The resource you requested could not be found",
            "statusCode": 404
        })

    @app.route("/")
    def hello_world():
        return jsonify({
            "version": "0.0.1"
        })

    return app
