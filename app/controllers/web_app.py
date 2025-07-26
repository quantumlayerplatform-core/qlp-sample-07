from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Welcome to the Web App')

@app.route('/data')
def fetch_data():
    # Simulated data fetch operation
    data = {
        'id': 123,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)