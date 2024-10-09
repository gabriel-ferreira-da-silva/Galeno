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