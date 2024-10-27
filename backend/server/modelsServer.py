import base64
from flask import Blueprint, jsonify, request, Response
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
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
    

@models_blueprint.route("/models/analysedata", methods=['POST'])
def analyse_data():
    try:
        if 'traindata' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        datafile = request.files['traindata']

        if datafile.filename == '':
            return jsonify({"error": "No file selected"}), 400

        df = pd.read_csv(datafile)
        print("DataFrame loaded:", df.head())  # Check DataFrame content
        
        correlation = df.corr()
        print("Correlation matrix calculated.")

        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title('Correlation Heatmap')

        img_corr = BytesIO()
        plt.savefig(img_corr, format='png')
        img_corr.seek(0)
        correlation_base64 = base64.b64encode(img_corr.getvalue()).decode('utf-8')
        plt.close()
        
        distribuitions = []
        boxplots = []
        numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
        print("Numeric columns:", numeric_columns)  # Check numeric columns
        
        for column in numeric_columns:
            plt.figure(figsize=(5, 4))
            sns.histplot(df[column], bins=30, kde=True)
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.title('Distribution of ' + column)
            
            img = BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            dist = base64.b64encode(img.getvalue()).decode('utf-8')
            distribuitions.append(dist)
            plt.close()

        for column in numeric_columns:
            plt.figure(figsize=(5, 4))
            sns.boxplot(data=df[column])
            plt.title('Box Plots for All Numerical Columns')
            plt.xticks(rotation=90)
            
            img = BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            boxplot = base64.b64encode(img.getvalue()).decode('utf-8')
            boxplots.append(boxplot)
            plt.close()

        print("Distributions generated:", len(distribuitions))  # Number of distributions generated
        return jsonify({"correlation": correlation_base64,
                        "distribuitions": distribuitions,
                        "boxplots": boxplots,
                        })

    except Exception as e:
        print("Error:", e) 
        return jsonify({'error': str(e)}), 500



@models_blueprint.route("/models/schema", methods=['GET'])
def get_models_schema():
    try:
        schema = getModelSchema()
        return jsonify(schema)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500