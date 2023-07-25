from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

@app.route('/namechecker', methods=['POST'])
def check_name():
    data = request.get_json()
    name_value = data.get('namevalue', '')

    name_pattern = r"^[a-zA-Z][a-zA-Z -]*[a-zA-Z]$"

    if re.match(name_pattern, name_value):
        response = {
            'success': True,
            'message': 'Name is valid.'
        }
    else:
        response = {
            'success': False,
            'message': 'Name is invalid.'
        }

    return jsonify(response)


@app.route('/apitest', methods=['GET'])
def test_api():
    response = {
        'message': "I'm working"
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
