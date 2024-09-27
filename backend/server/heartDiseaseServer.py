import numpy as np
from utils.heart_failure_utils import *
from bson.binary import Binary
from datetime import datetime
from flask import Blueprint, jsonify, request


base_url = "heartfailure"
heart_failure_model_blueprint = Blueprint('heartFailureModel_blueprint', __name__)


@heart_failure_model_blueprint.route(base_url + "/predict", methods=['POST'])
def heart_failure_predict():
    try:
        data = request.get_json()
        
        if not data or 'input_array' not in data or len(data['input_array']) != 11:
            return jsonify({'error': 'Invalid input. Provide an array of 11 numbers.'}), 400

        input_array = np.array(data['input_array'])
        
        heart_failure_mlp = load_heart_failure_mlp()
        
        prediction = heart_failure_mlp.predict(input_array.reshape(1, -1))

        print(input_array.reshape(1, -1) )

        results = {
            "disease": "heart failure",
            "model": "mlp",
            "modelname": "heart_failure_mlp",
            "result": prediction.tolist()
        }

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

        heart_failure_mlp = load_heart_failure_mlp()
        
        
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
