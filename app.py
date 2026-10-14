
from flask import Flask, jsonify, request

app = Flask(__name__)

# Home API endpoint
@app.route("/")
@app.route("/api")
def api_home():
    return "Welcome to my first API!"

# Student API endpoint
@app.route("/student")
def get_student():
    return jsonify({
        "student_id": "2024-0087",
        "name": "Kc Jane Marie Ladoing",
        "program": "BSIT",
        "year": 3,
        "section": "B"
    })

# Greeting API endpoint
@app.route("/hello")
def hello():
    name = request.args.get("name", "Student")
    return jsonify({
        "message": f"Hello, {name}!"
    })

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
