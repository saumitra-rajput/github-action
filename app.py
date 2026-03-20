from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    """Landing page route."""
    return render_template("index.html")


@app.route("/api/status")
def status():
    """Health check endpoint."""
    return jsonify({
        "status": "online",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "version": "1.0.0"
    })


@app.route("/api/hello")
def hello():
    """Sample API endpoint."""
    return jsonify({
        "message": "Hello, World!",
        "success": True
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)


