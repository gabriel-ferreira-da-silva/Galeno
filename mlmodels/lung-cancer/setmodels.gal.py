#!/usr/bin/env python3

import pymongo
from bson.binary import Binary
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['galeno_database']
models_collection = db['models']


with open('lung-cancer-mlp.pkl', 'rb') as f:
    lung_cancer_mlp_binary = f.read()

with open('lung-cancer-scaler.pkl', 'rb') as f:
    lung_cancer_scaler_binary = f.read()


lung_cancer_mlp_document = {
    "name": "lung-cancer-mlp",
    "disease": "heart failure",
    "type": "mlp",
    "last_update": datetime.now(),
    "input_description": ["ALLERGY", 	"WHEEZING",	"ALCOHOL CONSUMING",	"COUGHING","SHORTNESS OF BREATH",	"SWALLOWING DIFFICULTY", "CHEST PAIN","GENDER", "AGE",	"SMOKING",	"YELLOW_FINGERS",	"ANXIETY", "PEER_PRESSURE","CHRONIC DISEASE",	"FATIGUE"],
    "output_description": "0 = negative to lung cancer, 1 = positive to lung cancer",
    "model": Binary(lung_cancer_mlp_binary),
    "scaler": Binary(lung_cancer_scaler_binary)
}

result = models_collection.insert_one( lung_cancer_mlp_document)
print(f"Model inserted with _id: {result.inserted_id}")
