from .database_utils import *
from .commom_utils import *
from flask import jsonify


def request_is_valid(data):
    if not data or 'input_array' not in data  or len(data['input_array']) != 11:
        return False
    return True

def request_error():
    return jsonify({'error': 'Invalid input. Provide an array of 11 numbers.'}), 400
