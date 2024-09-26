import pymongo
import pickle

def load_models():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['galeno_database']
    models_collection = db['models']
    return models_collection


def load_model(model_name):
    models_collection = load_models()
    model_document = models_collection.find_one({"name": model_name})
    
    if model_document is None:
        raise FileNotFoundError("Model not found in the database")
    
    model_binary = model_document['model']
    neural_network = pickle.loads(model_binary)
    return neural_network
