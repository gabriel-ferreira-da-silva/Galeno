

from flask import Blueprint, jsonify, request
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