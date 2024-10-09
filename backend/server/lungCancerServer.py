import numpy as np
from flask import Blueprint, jsonify, request
from classes.lungcancer.lung_cancer_mlp import lung_cancer_mlp


base_url = "lungcancer"
lungCancerModel_blueprint = Blueprint('lungCancerModel_blueprint', __name__)

def request_is_valid(data):
    if not data or 'input_array' not in data  or len(data['input_array']) != 15:
        return False
    return True

def request_error():
    return jsonify({'error': 'Invalid input. Provide an array of 11 numbers.'}), 400


@lungCancerModel_blueprint.route(base_url + "/predict/mlp", methods=['POST'])
def lungCancerPredict():
    try:
        data = request.get_json()
        
        if request_is_valid(data) == False:
            return request_error()
        
        lc_mlp = lung_cancer_mlp()
        results = lc_mlp.get_results(data)
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@lungCancerModel_blueprint.route(base_url + "/train/mlp", methods=['POST'])
def train_lung_cancer_mlp():
    try:
        data = request.get_json()
        
        if not data or 'training_data' not in data:
            return jsonify({'error': 'Invalid input. Provide training data.'}), 400

        lc_mlp = lung_cancer_mlp()
        lc_mlp.train(data)
        return jsonify({'message': 'Model trained successfully.'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@lungCancerModel_blueprint.route(base_url + "/info/mlp", methods=['GET'])
def get_lung_cancer_mlp_info():
    try:
        lc_mlp = lung_cancer_mlp()
        return jsonify(lc_mlp.get_header()), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
