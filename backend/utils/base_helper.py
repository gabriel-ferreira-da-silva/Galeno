
from .database_utils import *
from flask import jsonify

class base_helper():

    def __init__(self):
        self.input_number = 0

    def request_is_valid(self,data):
        if not data or 'input_array' not in data  or len(data['input_array']) != self.input_number:
            return False
        return True

    def request_error(self):
        return jsonify({'error': 'Invalid input. Provide an array of 11 numbers.'}), 400
