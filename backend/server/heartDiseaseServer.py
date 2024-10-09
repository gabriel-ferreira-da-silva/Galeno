import utils.heart_failure_utils as hf
from utils.commom_utils import *
from utils.database_utils import *
from flask import Blueprint, jsonify, request
from classes.heartfailure.heart_failure_mlp import heart_failure_mlp
from classes.heartfailure.heart_failure_kmean import heart_failure_kmean
from classes.heartfailure.heart_failure_kmedoid import heart_failure_kmedoid


base_url = "heartfailure"
heart_failure_model_blueprint = Blueprint('heartFailureModel_blueprint', __name__)


@heart_failure_model_blueprint.route(base_url + "/predict/mlp", methods=['POST'])
def heart_failure_predict_mlp():
    try:
        data = request.get_json()
        
        if hf.request_is_valid(data) == False:
            return hf.request_error()
        
        hf_mlp = heart_failure_mlp()
        results = hf_mlp.get_results(data)
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@heart_failure_model_blueprint.route(base_url + "/predict/kmean", methods=['POST'])
def heart_failure_predict_kmean():
    try:
        data = request.get_json()
        
        if hf.request_is_valid(data) == False:
            return hf.request_error()
        
        hf_kmean = heart_failure_kmean()
        results = hf_kmean.get_results(data)
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@heart_failure_model_blueprint.route(base_url + "/predict/kmedoid", methods=['POST'])
def heart_failure_predict_kmedoid():
    try:
        data = request.get_json()
        
        if hf.request_is_valid(data) == False:
            return hf.request_error()
        
        hf_kmedoid = heart_failure_kmedoid()
        
        results = hf_kmedoid.get_results(data)
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@heart_failure_model_blueprint.route(base_url + "/train/mlp", methods=['POST'])
def train_heart_failure_mlp():
    try:
        data = request.get_json()
        
        if not data or 'training_data' not in data:
            return jsonify({'error': 'Invalid input. Provide training data.'}), 400

        lc_mlp = heart_failure_mlp()
        lc_mlp.train(data)
        return jsonify({'message': 'Model trained successfully.'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@heart_failure_model_blueprint.route(base_url + "/info/mlp", methods=['GET'])
@heart_failure_model_blueprint.route(base_url + "/info/kmean", methods=['GET'])
@heart_failure_model_blueprint.route(base_url + "/info/kmedoid", methods=['GET'])
def get_heart_failure_mlp_info():
    try:
        lc_mlp = heart_failure_mlp()
        return jsonify(lc_mlp.get_header()), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
