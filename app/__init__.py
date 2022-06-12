from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os



db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    env_config = os.getenv("APP_SETTINGS", "app.config.DevelopmentConfig")
    app.config.from_object(env_config)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    from . import models
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(
            {
                "error": "The resource you requested could not be found",
                "statusCode": 404,
            }
        )

    @app.route("/")
    def hello_world():
        return jsonify({"version": "0.0.1"})

    return app
