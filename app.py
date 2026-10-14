from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Web interface
@app.route("/")
def home():
    return render_template("index.html")

# Home API endpoint
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

if __name__ == "__main__":
    app.run(debug=True)
