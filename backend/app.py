from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <- this is mandatory for React frontend

@app.route("/")
def home():
    return jsonify({"message": "Hello IAM! Backend is alive 😎"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
