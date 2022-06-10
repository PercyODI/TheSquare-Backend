from flask import Flask, jsonify

app = Flask(__name__)


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
