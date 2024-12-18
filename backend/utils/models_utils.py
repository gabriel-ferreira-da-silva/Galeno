from datetime import datetime
import pymongo
import pickle
from bson.binary import Binary
from .diseases_utils import *

def loadModels():
    client = pymongo.MongoClient("mongodb://localhost:27017/",serverSelectionTimeoutMS=5000) 
    db = client['galeno_database']
    models_collection = db['models']
    return models_collection


def getModels():
    models_collection = loadModels()
    models = models_collection.find({}, {"name": 1, "description": 1, "type": 1, "disease": 1, "_id": 0})
    return list(models)


def getAvailableModels():
    collections = loadModels()
    distinct_names = collections.distinct('name')
    return distinct_names


def deleteModelByName(name):
    collections = loadModels()
    result = collections.delete_one({'name': name})
    
    
    if result.deleted_count == 0:
        print("No document found with that name.")

def insertModel(data):
    models = loadModels()
    required_fields = ["name", "type", "description", "disease", "output_description", "model"]
    print(data)
    for field in required_fields:
        if field not in data:
            print(f"Error: '{field}' is missing from input data.")
            return f"error: missing field '{field}'"

    print("Inserting model with the following details:")
    for key in ["name", "type", "model"]:
        print(f"{key}: {data[key]}")

    try:    
        new_model_document = {
            "name": data["name"],
            "type": data["type"],
            "description": data["description"],
            "disease": data["disease"],
            "last_update": datetime.now(),
            "output_description": data["output_description"],
            "model": Binary(data["model"]) if isinstance(data["model"], bytes) else None
        }
    except Exception as e:
        print("Error creating document:", e)
        return "error creating document"

    if new_model_document["model"] is None:
        print("Error: 'model' data is not in binary format.")
        return "error: model data not binary"

    try:
        result = models.insert_one(new_model_document)
    except Exception as e:
        print("Error inserting model:", e)
        return "error inserting model"

    print("Insertion result:", result.inserted_id)
    return result.inserted_id

def getModelsNamesByDisease(disease):
    collections = loadModels()
    distinct_names = collections.distinct('name',{'disease':disease})
    return distinct_names

def getModelByName(name):
    collections = loadModels()
    data = collections.find_one({'name':str(name)})
    document = {
            "name": data["name"],
            "type": data["type"],
            "description": data["description"],
            "disease": data["disease"],
            "last_update": datetime.now(),
            "output_description": data["output_description"],
        }
    return document


def getModelOutputDescriptionByName(name):
    collections = loadModels()
    distinct_names = collections.distinct('output_description',{'name':name})
    return distinct_names

def getModelDescriptionByName(name):
    collections = loadModels()
    distinct_names = collections.distinct('description',{'name':name})
    return distinct_names

def getModelSchema( sample_size=100):
    collection = loadModels()
    sample_documents = collection.find().limit(sample_size)
    schema = {}
    
    for document in sample_documents:
        for key, value in document.items():
            if key not in schema:
                schema[key] = str(type(value)).replace("<class '", "").replace("'>", "")
    
    return schema

def loadModel(model_name):
    models_collection = loadModels()
    model_document = models_collection.find_one({"name": model_name})
    
    if model_document is None:
        raise FileNotFoundError("Model not found in the database")
    
    model_binary = model_document['model']
    neural_network = pickle.loads(model_binary)
    return neural_network

def loadScaler(name):
    models_collection = loadDiseases()
    model_document = models_collection.find_one({"name": name})
    
    if model_document is None:
        raise FileNotFoundError("Model not found in the database")
    
    model_binary = model_document['scaler']
    scaler = pickle.loads(model_binary)
    return scaler
