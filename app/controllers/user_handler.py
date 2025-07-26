from flask import Flask, request, jsonify
from service.user_service import UserService

app = Flask(__name__)
user_service = UserService()

@app.route('/user', methods=['POST'])
def create_user():
    try:
        user_data = request.json
        result = user_service.create_user(user_data)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        result = user_service.get_user(user_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user_data = request.json
        result = user_service.update_user(user_id, user_data)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        result = user_service.delete_user(user_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)