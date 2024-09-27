import pymongo
from bson.binary import Binary
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['galeno_database']
models_collection = db['models']

with open('heart-failure-mlp.pkl', 'rb') as f:
    heart_failure_mlp_binary = f.read()

with open('heart-failure-kmean.pkl', 'rb') as f:
    heart_failure_kmean_binary = f.read()

with open('heart-failure-mlp.pkl', 'rb') as f:
    heart_failure_kmedoid_binary = f.read()


heart_failure_mlp_document = {
    "name": "heart-failure-mlp",
    "disease": "heart failure",
    "type": "mlp",
    "last_update": datetime.now(),
    "input_description": ', '.join(["Age","ChestPainType", "Cholesterol", "ExerciseAngina", "FastingBS",  "MaxHR", "Oldpeak","RestingBP",	"RestingECG", "Sex","ST_Slope"]),
    "output_description": "0 = negative to heart failure, 1 = positive to heart failure",
    "model": Binary(heart_failure_mlp_binary)
}

heart_failure_kmean_document = {
    "name": "heart-failure-kmean",
    "disease": "heart failure",
    "type": "kmean",
    "last_update": datetime.now(),
    "input_description": ', '.join(["Age","ChestPainType", "Cholesterol", "ExerciseAngina", "FastingBS",  "MaxHR", "Oldpeak","RestingBP",	"RestingECG", "Sex","ST_Slope"]),
    "output_description": "0 = high probability of positive to heart failure , 1 = inconclusive",
    "model": Binary(heart_failure_kmean_binary)
}

heart_failure_kmedoid_document = {
    "name": "heart-failure-kmedoid",
    "disease": "heart failure",
    "type": "kmedoid",
    "last_update": datetime.now(),
    "input_description": ', '.join(["Age","ChestPainType", "Cholesterol", "ExerciseAngina", "FastingBS",  "MaxHR", "Oldpeak","RestingBP",	"RestingECG", "Sex","ST_Slope"]),
    "output_description": "0 = high probability of positive to heart failure , 1 = inconclusive",
    "model": Binary(heart_failure_mlp_binary)
}

result = models_collection.insert_one( heart_failure_mlp_document)
print(f"Model inserted with _id: {result.inserted_id}")

result = models_collection.insert_one( heart_failure_kmean_document)
print(f"Model inserted with _id: {result.inserted_id}")

result = models_collection.insert_one( heart_failure_kmedoid_document)
print(f"Model inserted with _id: {result.inserted_id}")

