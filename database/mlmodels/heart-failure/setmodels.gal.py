#!/usr/bin/env python3

import pymongo
from bson.binary import Binary
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['galeno_database']
models_collection = db['models']
diseases_collection = db['diseases']


with open('setupfiles/heart-failure-kmean.pkl', 'rb') as f:
    heart_failure_kmean_binary = f.read()

with open('setupfiles/heart-failure-mlp.pkl', 'rb') as f:
    heart_failure_mlp_binary = f.read()

with open('setupfiles/heart-failure-kmedoid.pkl', 'rb') as f:
    heart_failure_kmedoid_binary = f.read()

with open('setupfiles/heart-failure-scaler.pkl', 'rb') as f:
    heart_failure_scaler_binary = f.read()

disease = "heart failure"
heart_failure_disease_document = {
    "name": disease,
    "description":""""
  \n  
    People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.
\n
    Attribute Information\n
\n

    Age: age of the patient [years]\n
    Sex: sex of the patient [M: Male, F: Female]\n
    ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
    \nRestingBP: resting blood pressure [mm Hg]\n
    Cholesterol: serum cholesterol [mm/dl]\n
    FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]\n
    RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]\n
    MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]\n
    ExerciseAngina: exercise-induced angina [Y: Yes, N: No]\n
    Oldpeak: oldpeak = ST [Numeric value measured in depression]\n
    ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]\n
    HeartDisease: output class [1: heart disease, 0: Normal]\n
    """,

    "disease": disease,
    "input_description": [
                {
                    "input": "age",
                    "description": "age of the patient [years]"
                },
                {
                    "input": "Chest pain type",
                    "description": "[3: Typical Angina, 0: Atypical Angina, 1: Non-Anginal Pain, 2: Asymptomatic]"
                },
                {
                    "input": "cholesterol",
                    "description": "serum cholesterol [mm/dl]"
                },
                {
                    "input": "Exercise Angina",
                    "description": "exercise-induced angina [1: Yes, 0: No]"
                },
                {
                    "input": "Fasting BS",
                    "description": "fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]"
                },
                {
                    "input": "maximun HR",
                    "description": "maximum heart rate achieved [Numeric value between 60 and 202]"
                },
                {
                    "input": "oldpeak",
                    "description": "ST [Numeric value measured in depression]"
                },
                {
                    "input": "Resting BP",
                    "description": "[3: Typical Angina, 0: Atypical Angina, 1: Non-Anginal Pain, 2: Asymptomatic]"
                },
                {
                    "input": "RestingECG",
                    "description": "resting electrocardiogram results [0: Normal, 1: having ST-T wave abnormality, 2: showing probable or definite left ventricular hypertrophy by Estes' criteria]"
                },
                {
                    "input": "Sex",
                    "description": "sex of the patient [1: Male, 0: Female]"
                },
                {
                    "input": "ST_Slope",
                    "description": "the slope of the peak exercise ST segment [0: upsloping, 1: flat, 2: downsloping]"
                }
            ],
    "scaler": Binary(heart_failure_scaler_binary)
}


heart_failure_mlp_document = {
    "name": "heart-failure-mlp",
    "disease": disease,
    "description": "heart-failure-mlp is a multilayer perceptron classifier trained with kaggle heart failure dataset https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction",
    "type": "mlp",
    "last_update": datetime.now(),
    "output_description": "0 = negative to heart failure, 1 = positive to heart failure",
    "model": Binary(heart_failure_mlp_binary)
}

heart_failure_kmean_document = {
    "name": "heart-failure-kmean",
    "disease": "heart failure",
    "description": "heart-failure-kmeans is a kmeans cluster classifier trained with kaggle heart failure dataset https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction",
    "type": "kmean",
    "last_update": datetime.now(),
    "output_description": "0 = high probability of positive to heart failure , 1 = inconclusive",
    "model": Binary(heart_failure_kmean_binary)
}

heart_failure_kmedoid_document = {
    "name": "heart-failure-kmedoid",
    "disease": "heart failure",
    "description": "heart-failure-kmedoid is a kmedoid cluster classifier trained with kaggle heart failure dataset https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction",
    "type": "kmedoid",
    "last_update": datetime.now(),
    "output_description": "0 = high probability of positive to heart failure , 1 = inconclusive",
    "model": Binary(heart_failure_kmedoid_binary)
}

result = diseases_collection.insert_one( heart_failure_disease_document)
print(f"Model inserted with _id: {result.inserted_id}")

result = models_collection.insert_one( heart_failure_mlp_document)
print(f"Model inserted with _id: {result.inserted_id}")

result = models_collection.insert_one( heart_failure_kmean_document)
print(f"Model inserted with _id: {result.inserted_id}")

result = models_collection.insert_one( heart_failure_kmedoid_document)
print(f"Model inserted with _id: {result.inserted_id}")
