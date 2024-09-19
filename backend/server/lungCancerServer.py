from flask import Blueprint, jsonify, request
import pymongo
import gridfs
import pickle
import numpy as np
from connection.dbconn import fs

base_url = "lungcancer"
lungCancerModel_blueprint = Blueprint('lungCancerModel_blueprint', __name__)


def load_lung_cancer_mlp():
    file_data = fs.find_one({"filename": "lung-cancer-mlp.pkl"})
    
    if file_data is None:
        raise FileNotFoundError("Model not found in the database")
    
    file_content = file_data.read()
    neural_network = pickle.loads(file_content)
    return neural_network



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
