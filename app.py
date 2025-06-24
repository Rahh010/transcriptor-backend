from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask on Render!"})

@app.route('/api/data', methods=['POST'])
def data():
    name = request.json.get('name', 'Guest')
    return jsonify({"reply": f"Hi, {name}!"})

if __name__ == '__main__':
    app.run()
