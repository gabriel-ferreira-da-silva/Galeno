

from flask import Blueprint, jsonify, request
import numpy as np

from utils.models_utils import *
from utils.diseases_utils import *

models_blueprint = Blueprint('models_blueprint', __name__)


@models_blueprint.route("/models", methods=['GET'])
def get_models():
    try:
        diseases = getAvailableModels()
        return jsonify(diseases)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@models_blueprint.route("/models/bydisease/<disease>", methods=['GET'])
def get_models_name_by_disaese(disease):
    try:
        names = getModelsNamesByDisease(disease)
        return jsonify(names)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@models_blueprint.route("/models/byname/<name>", methods=['GET'])
def get_model_by_name(name):
    try:
        model = getModelByName(str(name))
        return jsonify(model)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@models_blueprint.route("/models/add", methods=['POST'])
def insert_new_model():
    try:
        
        data = {
            "name": request.form.get("name"),
            "type": request.form.get("type"),
            "description": request.form.get("description"),
            "disease": request.form.get("disease"),
            "output_description": request.form.get("output_description"),
        }

        
        file = request.files.get("model")
        if file:
            data["model"] = Binary(file.read())
        else:
            return jsonify({"error": "Model file is missing"}), 400

        
        result = insertModel(data)
        print(result)

        
        return jsonify({"result": result}), 201
    except Exception as e:
        print("Error adding model:", e)
        return jsonify({"error": "Failed to add new model"}), 500
    

@models_blueprint.route("/models/predict", methods=['POST'])
def predict_by_model():
    try:
        data = request.get_json()
        input = data["input"]
        name = data["name"]

        print(input)
        print(name)

        mlmodel = loadModel(name)
        input = np.array(input)
        res = mlmodel.predict(input.reshape(1,-1))
        output_description = getModelOutputDescriptionByName(name)
        model_description=""
        try:
            model_description = getModelDescriptionByName(name)
        except Exception as e:
            model_description = "Error fetching model description"

        return jsonify({"res":res.tolist(),"output_description":output_description, "model_description": model_description })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@models_blueprint.route("/models/schema", methods=['GET'])
def get_models_schema():
    try:
        schema = getModelSchema()
        return jsonify(schema)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500