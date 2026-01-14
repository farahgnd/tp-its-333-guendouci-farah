from flask import Flask, request, jsonify
import json
import requests
from functools import wraps
import jwt

app = Flask(__name__)
DATA_FILE = 'data.json'
PERSON_SERVICE_URL = "http://person-service:5001/persons"



SECRET_KEY = "monsecretjwt123"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({"error": "Token is missing"}), 401
        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated

 # Docker network

# Charger les données
try:
    with open(DATA_FILE) as f:
        health_data = json.load(f)
except FileNotFoundError:
    health_data = {}

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(health_data, f)

def person_exists(person_id):
    response = requests.get(f'{PERSON_SERVICE_URL}/{person_id}')
    return response.status_code == 200

@app.route('/health/<int:person_id>', methods=['GET'])
@token_required
def get_health(person_id):
    if not person_exists(person_id):
        return jsonify({"error": "Person not found"}), 404
    data = health_data.get(str(person_id))
    if not data:
        return jsonify({"error": "Health data not found"}), 404
    return jsonify(data)

@app.route('/health/<int:person_id>', methods=['POST'])
@token_required
def add_health(person_id):
    if not person_exists(person_id):
        return jsonify({"error": "Person not found"}), 404
    data = request.json
    health_data[str(person_id)] = data
    save_data()
    return jsonify(data), 201

@app.route('/health/<int:person_id>', methods=['PUT'])
@token_required
def update_health(person_id):
    if not person_exists(person_id):
        return jsonify({"error": "Person not found"}), 404
    data = request.json
    health_data[str(person_id)] = data
    save_data()
    return jsonify(data)

@app.route('/health/<int:person_id>', methods=['DELETE'])
@token_required
def delete_health(person_id):
    if not person_exists(person_id):
        return jsonify({"error": "Person not found"}), 404
    if str(person_id) in health_data:
        del health_data[str(person_id)]
        save_data()
        return jsonify({"message": "Health data deleted"})
    return jsonify({"error": "Health data not found"}), 404






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
