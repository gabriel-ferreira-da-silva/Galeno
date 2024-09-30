import pymongo
from bson.binary import Binary
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['galeno_database']
models_collection = db['models']

with open('breast-cancer-gaussian.pkl', 'rb') as f:
    breast_cancer_gaussian_binary = f.read()

breast_cancer_gaussian_document = {
    "name": "breast_cancer_gpr",
    "disease": "breast-cancer",
    "type": "gpr",
    "last_update": datetime.now(),
    "input_description": ', '.join([
                                    "area_mean",
                                    "area_se",
                                    "area_worst",
                                    "compactness_mean",
                                    "compactness_se",
                                    "compactness_worst",
                                    "concave points_mean",
                                    "concave points_se",
                                    "concave points_worst",
                                    "concavity_mean",
                                    "concavity_se",
                                    "concavity_worst",
                                    "fractal_dimension_mean",
                                    "fractal_dimension_se",
                                    "fractal_dimension_worst",
                                    "perimeter_mean",
                                    "perimeter_se",
                                    "perimeter_worst",
                                    "radius_mean",
                                    "radius_se",
                                    "radius_worst",
                                    "smoothness_mean",
                                    "smoothness_se",
                                    "smoothness_worst",
                                    "symmetry_mean",
                                    "symmetry_se",
                                    "symmetry_worst",
                                    "texture_mean",
                                    "texture_se",
                                    "texture_worst"
                                ]),
    "output_description": "0 = negative to , 1 = positive ",
    "model": Binary(breast_cancer_gaussian_binary)
}


result = models_collection.insert_one( breast_cancer_gaussian_document)
print(f"Model inserted with _id: {result.inserted_id}")

