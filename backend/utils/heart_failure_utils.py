import numpy as np
from .database_utils import *
from .commom_utils import *
from flask import jsonify

def load_mlp():
    heart_failure_mlp = load_model("heart-failure-mlp")
    return heart_failure_mlp

def request_is_valid(data):
    if not data or 'input_array' not in data  or len(data['input_array']) != 11:
        return False
    return True

def request_error():
    return jsonify({'error': 'Invalid input. Provide an array of 11 numbers.'}), 400

def mlp_predict(input):
    input_array = np.array(input)
    heart_failure_mlp = load_mlp()
    prediction = heart_failure_mlp.predict(input_array.reshape(1, -1))
    return prediction

def mlp_format_results(prediction):
    results = {
            "disease": "heart failure",
            "model": "mlp",
            "modelname": "heart_failure_mlp",
            "result": prediction.tolist()
        }
    return results

def mlp_get_results(data):
    input = data['input_array']
    prediction = mlp_predict(input)
    results = mlp_format_results(prediction)
    return results
