#!/usr/bin/env python3

import pymongo
from bson.binary import Binary
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['galeno_database']
models_collection = db['models']
diseases_collection = db['diseases']


with open('setupfiles/lung-cancer-mlp.pkl', 'rb') as f:
    lung_cancer_mlp_binary = f.read()

with open('setupfiles/lung-cancer-scaler.pkl', 'rb') as f:
    lung_cancer_scaler_binary = f.read()


disease="lung cancer"
lung_cancer_disease_document = {
    "name": disease,
    "description" : '''
    
    The effectiveness of cancer prediction system helps the people to know their cancer risk with low cost and it also helps the people to take the appropriate decision based on their cancer risk status. The data is collected from the website online lung cancer prediction system .
\n
    Total no. of attributes:16
    No .of instances:284\n
    Attribute information:
\n
    Gender: M(male), F(female)\n
    Age: Age of the patient\n
    Smoking: YES=2 , NO=1.\n
    Yellow fingers: YES=2 , NO=1.\n
    Anxiety: YES=2 , NO=1.\n
    Peer_pressure: YES=2 , NO=1.\n
    Chronic Disease: YES=2 , NO=1.\n
    Fatigue: YES=2 , NO=1.\n
    Allergy: YES=2 , NO=1.\n
    Wheezing: YES=2 , NO=1.\n
    Alcohol: YES=2 , NO=1.\n
    Coughing: YES=2 , NO=1.\n
    Shortness of Breath: YES=2 , NO=1.\n
    Swallowing Difficulty: YES=2 , NO=1.\n
    Chest pain: YES=2 , NO=1.\n
    Lung Cancer: YES , NO.\n
\n
    ''',
    
    "disease": disease,
    "input_description": [
            {
                "input":"AGE",
                "description":"age in years",
            },
            {
                "input":"ALCOHOL CONSUMING",
                "description":"1 to no 2 to yes"
            },
            {
                "input":"ALLERGY",  
                "description":"1 to no 2 to yes"
            },
            {
                "input":"ANXIETY",  
                "description":"1 to no 2 to yes"
            },
            {
                "input":"CHEST PAIN",  
                "description":"1 to no 2 to yes"
            },
            {
                "input":"CHRONIC DISEASE",
                "description":"1 to no 2 to yes"
            },
            {
                "input":"COUGHING",
                "description":"1 to no 2 to yes"
            },
            {
                "input":"FATIGUE",  
                "description":"1 to no 2 to yes"
            },
            {
                "input":"GENDER",
                "description":"1 to no 2 to yes"
            },
            {
                "input":"PEER PRESSURE",  
                "description":"1 to no 2 to yes"
            },
            
            {
                "input":"SHORTNESS OF BREATH",  
                "description":"1 to no 2 to yes"
            },
            {
                "input":"SMOKING",  
                "description":"1 to no 2 to yes"
            },
            {
                "input":"SWALLOWING DIFFICULTY",  
                "description":"1 to no 2 to yes"
            },
            {
                "input":"WHEEZING",  
                "description":"1 to no 2 to yes"
            },
            {
                "input":"YELLOW FINGERS", 
                "description":"1 to no 2 to yes"
            },
        ],
    "scaler": Binary(lung_cancer_scaler_binary)
}

lung_cancer_mlp_document = {
    "name": "lung-cancer-mlp",
    "description":"lun-cancer-mlp is a multilayer perceptron neural network trained with kaggle lung cancer dataset https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer.",
    "disease": disease,
    "type": "mlp",
    "last_update": datetime.now(),
    "output_description": "0 = negative to lung cancer, 1 = positive to lung cancer",
    "model": Binary(lung_cancer_mlp_binary)
}

result = diseases_collection.insert_one( lung_cancer_disease_document)
print(f"Model inserted with _id: {result.inserted_id}")


result = models_collection.insert_one( lung_cancer_mlp_document)
print(f"Model inserted with _id: {result.inserted_id}")
