import numpy as np
import utils.heart_failure_utils as hf
from utils.commom_utils import *
from utils.database_utils import *
from bson.binary import Binary
from datetime import datetime
from flask import Blueprint, jsonify, request

base_url = "heartfailure"
heart_failure_model_blueprint = Blueprint('heartFailureModel_blueprint', __name__)


@heart_failure_model_blueprint.route(base_url + "/predict/mlp", methods=['POST'])
def heart_failure_predict():
    try:
        data = request.get_json()
        
        if hf.request_is_valid(data) == False:
            return hf.request_error()
        
        results = hf.mlp_get_results(data)
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@heart_failure_model_blueprint.route(base_url + "/train", methods=['POST'])
def train_lung_cancer_mlp():
    try:
        data = request.get_json()
        
        if not data or 'training_data' not in data:
            return jsonify({'error': 'Invalid input. Provide training data.'}), 400

        training_data = np.array(data['training_data'])
        
        if training_data.shape[1] != 12:
            return jsonify({'error': 'Each input array must have 16 elements.'}), 400

        X = training_data[:, :-1]
        y = training_data[:, -1]  

        heart_failure_mlp = hf.load_mlp()
        
        
        heart_failure_mlp.fit(X, y)

        models_collection = load_models()
        model_binary = pickle.dumps(heart_failure_mlp)
        models_collection.update_one(
            {"name": "heart-failure-mlp"},
            {"$set": {"model": Binary(model_binary), "last_update": datetime.now()}}
        )

        return jsonify({'message': 'Model trained successfully.'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
