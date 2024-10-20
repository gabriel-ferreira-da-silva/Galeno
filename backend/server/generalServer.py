
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

@general_blueprint.route("/diseases/inputdescription/<name>", methods=['GET'])
def get_disease_input_by_name(name):
    try:
        input = get_diseases_input_description_by_name(name)
        return jsonify(input)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@general_blueprint.route("/models/predict", methods=['POST'])
def predict_by_model():
    try:
        data = request.get_json()
        input = data["input"]
        name = data["name"]

        print(input)
        print(name)

        mlmodel = load_model(name)
        input = np.array(input)
        res = mlmodel.predict(input.reshape(1,-1))
        output_description = get_models_output_description_by_name(name)
        model_description=""
        try:
            model_description = get_models_description_by_name(name)
        except Exception as e:
            model_description = "Error fetching model description"

        return jsonify({"res":res.tolist(),"output_description":output_description, "model_description": model_description })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@general_blueprint.route("/diseases/description/<disease>", methods=['GET'])
def get_disease_description_by_disease(disease):
    try:
        description = get_diseases_description_by_name(disease)
        return jsonify(description)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


@general_blueprint.route("/models/schema", methods=['GET'])
def get_models_schema():
    try:
        schema = get_model_schema()
        return jsonify(schema)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500