from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/cities')
def cities():
    city_data = {'cities': ['New York', 'London', 'Tokyo']}
    return jsonify(city_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)