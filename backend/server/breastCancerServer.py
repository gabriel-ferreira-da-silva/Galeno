from utils.commom_utils import *
from utils.database_utils import *
from flask import Blueprint, jsonify, request
from classes.breastcancer.breast_cancer_gpr import breast_cancer_gpr


base_url = "breastcancer"
breast_cancer_model_blueprint = Blueprint('breastCancerModel_blueprint', __name__)

def request_is_valid(data):
    if not data or 'input_array' not in data  or len(data['input_array']) != 30:
        return False
    return True

def request_error():
    return jsonify({'error': 'Invalid input. Provide an array of 11 numbers.'}), 400


@breast_cancer_model_blueprint.route(base_url + "/predict/gpr", methods=['POST'])
def heart_failure_predict_mlp():
    try:
        data = request.get_json()
        
        if request_is_valid(data) == False:
            return request_error()
        
        bc_gpr = breast_cancer_gpr()
        results = bc_gpr.get_results(data)
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@breast_cancer_model_blueprint.route(base_url + "/train/gpr", methods=['POST'])
def train_breast_cancer_mlp():
    try:
        data = request.get_json()
        
        if not data or 'training_data' not in data:
            return jsonify({'error': 'Invalid input. Provide training data.'}), 400

        lc_mlp = breast_cancer_gpr()
        lc_mlp.train(data)
        return jsonify({'message': 'Model trained successfully.'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@breast_cancer_model_blueprint.route(base_url + "/info/gpr", methods=['GET'])
def get_breast_cancer_info():
    try:
        lc_mlp = breast_cancer_gpr()
        return jsonify(lc_mlp.get_header()), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500