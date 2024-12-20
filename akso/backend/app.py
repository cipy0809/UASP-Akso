from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint untuk home
@app.route('/')
def home():
    return jsonify(message="Welcome to the Backend API"), 200

# Contoh endpoint untuk mendapatkan data
@app.route('/data', methods=['GET'])
def get_data():
    sample_data = {
        "id": 1,
        "name": "Sample Data",
        "description": "This is an example response from the backend API."
    }
    return jsonify(sample_data), 200

# Endpoint untuk menerima POST request
@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    if not data:
        return jsonify(error="No data provided"), 400
    return jsonify(message="Data received", data=data), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
