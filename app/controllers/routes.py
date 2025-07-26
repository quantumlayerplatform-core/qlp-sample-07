from .main import app
from flask import jsonify

@app.route('/api/example', methods=['GET'])
def example_route():
    return jsonify({"message": "This is an example route"})