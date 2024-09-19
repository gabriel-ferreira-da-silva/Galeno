import pickle

with open('lung-cancer-mlp.pkl', 'rb') as f:
    model_binary = f.read()


import pymongo
from bson.binary import Binary
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['galeno_database']
models_collection = db['models']

model_document = {
    "name": "lung-cancer-mlp",
    "disease": "lung cancer",
    "type": "mlp",
    "last_update": datetime.now(),
    "input_description": "15 numbers within 0,1",
    "output_description": "0 = negative to lung cancer, 1 = positive to lung cancer",
    "model": Binary(model_binary)
}

result = models_collection.insert_one(model_document)
print(f"Model inserted with _id: {result.inserted_id}")
