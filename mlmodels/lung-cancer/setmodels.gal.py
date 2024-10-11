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
    "description":"age is in years and the others input are 1 for no and 2 for yes",
    "disease": "heart failure",
    "type": "mlp",
    "last_update": datetime.now(),
    "input_description": [
            "AGE",  
            "ALCOHOL CONSUMING",  
            "ALLERGY",  
            "ANXIETY",  
            "CHEST PAIN",  
            "CHRONIC DISEASE", 
            "COUGHING",
            "FATIGUE",  
            "GENDER",  
            "PEER PRESSURE",  
            "SHORTNESS OF BREATH",  
            "SMOKING",  
            "SWALLOWING DIFFICULTY",  
            "WHEEZING",  
            "YELLOW FINGERS"
        ],
    "output_description": "0 = negative to lung cancer, 1 = positive to lung cancer",
    "model": Binary(lung_cancer_mlp_binary),
    "scaler": Binary(lung_cancer_scaler_binary)
}

result = models_collection.insert_one( lung_cancer_mlp_document)
print(f"Model inserted with _id: {result.inserted_id}")
