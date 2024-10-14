from utils.commom_utils import *
from utils.database_utils import *
from flask import Blueprint, jsonify, request
import numpy as np

general_blueprint = Blueprint('general_blueprint', __name__)


@general_blueprint.route("/diseases", methods=['GET'])
def get_diseases():
    try:
        diseases = get_available_diseases()
        return jsonify(diseases)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@general_blueprint.route("/models", methods=['GET'])
def get_models():
    try:
        diseases = get_available_models()
        return jsonify(diseases)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@general_blueprint.route("/models/<disease>", methods=['GET'])
def get_models_name_by_disaese(disease):
    try:
        diseases = get_models_names_by_disease(disease)
        return jsonify(diseases)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@general_blueprint.route("/models/inputdescription/<name>", methods=['GET'])
def get_models_input_by_name(name):
    try:
        input = get_models_input_description_by_name(name)
        return jsonify(input)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@general_blueprint.route("/models/predict", methods=['POST'])
def predict_by_model():
    try:
        data = request.get_json()
        input = data["input"]
        name = data["name"]

        mlmodel = load_model(name)
        input = np.array(input)
        res = mlmodel.predict(input.reshape(1,-1))
        output_description = get_models_output_description_by_name(name)

        return jsonify({"res":res.tolist(),"output_description":output_description})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500