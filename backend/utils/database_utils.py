import pymongo
import pickle

def load_models():
    client = pymongo.MongoClient("mongodb://localhost:27017/",serverSelectionTimeoutMS=5000) 
    db = client['galeno_database']
    models_collection = db['models']
    return models_collection


def load_diseases():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['galeno_database']
    diseases_collection = db['diseases']
    return diseases_collection


def get_available_diseases():
    collections = load_models()
    distinct_names = collections.distinct('disease')
    return distinct_names

def get_available_models():
    collections = load_models()
    distinct_names = collections.distinct('name')
    return distinct_names

def get_models_names_by_disease(disease):
    collections = load_models()
    distinct_names = collections.distinct('name',{'disease':disease})
    return distinct_names

def get_diseases_description_by_name(name):
    collections = load_diseases()
    distinct_names = collections.distinct('description',{'name':name})
    return distinct_names

def get_diseases_input_description_by_name(name):
    collections = load_diseases()
    distinct_names = collections.distinct('input_description',{'name':name})
    return distinct_names

def get_models_output_description_by_name(name):
    collections = load_models()
    distinct_names = collections.distinct('output_description',{'name':name})
    return distinct_names

def get_models_description_by_name(name):
    collections = load_models()
    distinct_names = collections.distinct('description',{'name':name})
    return distinct_names

def get_model_schema( sample_size=100):
    collection = load_models()
    sample_documents = collection.find().limit(sample_size)
    schema = {}
    
    for document in sample_documents:
        for key, value in document.items():
            if key not in schema:
                schema[key] = str(type(value)).replace("<class '", "").replace("'>", "")
    
    return schema

def load_model(model_name):
    models_collection = load_models()
    model_document = models_collection.find_one({"name": model_name})
    
    if model_document is None:
        raise FileNotFoundError("Model not found in the database")
    
    model_binary = model_document['model']
    neural_network = pickle.loads(model_binary)
    return neural_network

def load_scaler(model_name):
    models_collection = load_models()
    model_document = models_collection.find_one({"name": model_name})
    
    if model_document is None:
        raise FileNotFoundError("Model not found in the database")
    
    model_binary = model_document['scaler']
    neural_network = pickle.loads(model_binary)
    return neural_network

def get_model_object(model_name):
    models_collection = load_models()
    object = models_collection.find_one({"name": model_name})
    
    if object is None:
        raise FileNotFoundError("Model not found in the database")
    
    object['scaler'] = load_scaler(model_name)
    object['model'] = load_model(model_name)
    return object