
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!doctype html>
    <html>
    <head>
        <title>DockerDemo</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 80px;">
        <h1>DockerDemo is running!</h1>
        <p>This Flask application is running inside a Docker container.</p>
        <p>DevOps Assignment 4</p>
        <a href="/health">Check application health</a>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
