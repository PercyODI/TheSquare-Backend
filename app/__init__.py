from flask import Flask, jsonify
import os

def create_app(test_config=None):
    app = Flask(__name__)
    env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(env_config)

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
    @app.route("/dburl")
    def dburl():
        return jsonify({
            "dburl": app.config.get("DATABASE_URL")
        })

    return app
