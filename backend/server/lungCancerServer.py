import numpy as np
from utils.lung_cancer_utils import *
from bson.binary import Binary
from datetime import datetime
from flask import Blueprint, jsonify, request


base_url = "lungcancer"
lungCancerModel_blueprint = Blueprint('lungCancerModel_blueprint', __name__)


@lungCancerModel_blueprint.route(base_url + "/predict", methods=['POST'])
def lungCancerPredict():
    try:
        data = request.get_json()
        
        if not data or 'input_array' not in data or len(data['input_array']) != 15:
            return jsonify({'error': 'Invalid input. Provide an array of 15 numbers.'}), 400

        input_array = np.array(data['input_array'])
        
        lung_cancer_mlp = load_lung_cancer_mlp()
        
        prediction = lung_cancer_mlp.predict(input_array.reshape(1, -1))

        results = {
            "disease": "lung cancer",
            "model": "mlp",
            "modelname": "lung_cancer_mlp",
            "result": prediction.tolist()
        }

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
