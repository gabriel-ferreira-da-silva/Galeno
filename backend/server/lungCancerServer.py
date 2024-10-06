import numpy as np
from bson.binary import Binary
from datetime import datetime
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


@lungCancerModel_blueprint.route(base_url + "/train", methods=['POST'])
def train_lung_cancer_mlp():
    try:
        data = request.get_json()
        
        if not data or 'training_data' not in data:
            return jsonify({'error': 'Invalid input. Provide training data.'}), 400

        training_data = np.array(data['training_data'])
        
        if training_data.shape[1] != 16:
            return jsonify({'error': 'Each input array must have 16 elements.'}), 400

        X = training_data[:, :-1]
        y = training_data[:, -1]  

        lung_cancer_mlp = load_lung_cancer_mlp()
        
        
        lung_cancer_mlp.fit(X, y)

        models_collection = load_models()
        model_binary = pickle.dumps(lung_cancer_mlp)
        models_collection.update_one(
            {"name": "lung-cancer-mlp"},
            {"$set": {"model": Binary(model_binary), "last_update": datetime.now()}}
        )

        return jsonify({'message': 'Model trained successfully.'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
