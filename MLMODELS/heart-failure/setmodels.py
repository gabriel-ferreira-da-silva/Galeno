import pymongo
from bson.binary import Binary
from datetime import datetime
import pickle

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['galeno_database']
models_collection = db['models']


with open('heart-failure-mlp.pkl', 'rb') as f:
    model_binary = f.read()


model_document = {
    "name": "heart-failure-mlp",
    "disease": "heart failure",
    "type": "mlp",
    "last_update": datetime.now(),
    "input_description": "15 numbers within 0,1",
    "output_description": "0 = negative to heart failure, 1 = positive to heart failure",
    "model": Binary(model_binary)
}

result = models_collection.insert_one(model_document)
print(f"Model inserted with _id: {result.inserted_id}")