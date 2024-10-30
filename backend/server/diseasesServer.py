

from flask import Blueprint, json, jsonify, request
import numpy as np

from utils.models_utils import *
from utils.diseases_utils import *

diseases_blueprint = Blueprint('diseases_blueprint', __name__)

@diseases_blueprint.route("/diseases", methods=['GET'])
def get_diseases():
    try:
        diseases = getAvailableDiseases()
        return jsonify(diseases)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@diseases_blueprint.route("/diseases/inputdescription/<name>", methods=['GET'])
def get_disease_input_by_name(name):
    try:
        descriptions = getDiseasesInputDescriptionByName(name)
        return jsonify(descriptions)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@diseases_blueprint.route("/diseases/description/<disease>", methods=['GET'])
def get_disease_description_by_disease(disease):
    try:
        description = getDiseasesDescriptionByName(disease)
        return jsonify(description)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    



@diseases_blueprint.route("/diseases/add", methods=['POST'])
def insert_new_disease():
    try:
        
        input_description = request.form.get("input_description")
        
        
        try:
            input_description = json.loads(input_description)
        except (TypeError, ValueError) as e:
            return jsonify({"error": "Invalid format for input_description"}), 400

        
        data = {
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "disease": request.form.get("disease"),
            "input_description": input_description,
        }

        file = request.files.get("scaler")
        if file:
            data["scaler"] = Binary(file.read())
        else:
            return jsonify({"error": "Scaler file is missing"}), 400

        result = insertDisease(data)
        print(result)
        
        return jsonify({"result": result}), 201
    
    except Exception as e:
        print("Error adding disease:", e)
        return jsonify({"error": "Failed to add new disease"}), 500
             