from datetime import datetime
import pymongo
import pickle
from bson.binary import Binary
from .models_utils import *


def loadDiseases():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['galeno_database']
    diseases_collection = db['diseases']
    return diseases_collection

def getDiseasesDescriptionByName(name):
    collections = loadDiseases()
    distinct_names = collections.distinct('description',{'name':name})
    return distinct_names

def getDiseasesInputDescriptionByName(name):
    collections = loadDiseases()
    distinct_names = collections.distinct('input_description',{'name':name})
    return distinct_names


def getAvailableDiseases():
    collections = loadDiseases()
    distinct_names = collections.distinct('name')
    return distinct_names

def insertDisease(data):
    diseases = loadDiseases()
    required_fields = ["name", "description", "disease", "input_description", "scaler"]

    for field in required_fields:
        if field not in data:
            print(f"Error: '{field}' is missing from input data.")
            return f"error: missing field '{field}'"

    print("Inserting disease with the following details:")
    for key in ["name", "disease", "scaler"]:
        print(f"{key}: {data[key]}")

    # Prepare the document for insertion
    new_disease_document = {
        "name": data["name"],
        "description": data["description"],
        "disease": data["disease"],
        "input_description": data["input_description"],  # This should be an array of {input, description}
        "scaler": data["scaler"]  # Binary data is already processed
    }

    try:
        # Insert the document into the collection
        result = diseases.insert_one(new_disease_document)
    except Exception as e:
        print("Error inserting disease:", e)
        return "error inserting disease"

    print("Insertion result:", result.inserted_id)
    return str(result.inserted_id)