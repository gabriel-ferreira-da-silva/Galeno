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