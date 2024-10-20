#!/usr/bin/env python3

import pymongo
from bson.binary import Binary
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['galeno_database']
models_collection = db['models']
diseases_collection = db['diseases']

with open('setup/breast_cancer_gaussian.pkl', 'rb') as f:
    breast_cancer_gaussian_binary = f.read()

with open('setup/breast-cancer-scaler.pkl', 'rb') as f:
    breast_cancer_scaler_binary = f.read()
disease = "breast cancer"


breast_cancer_disease_document = {
    "name": disease,
    "description":""""
        Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image.
    n the 3-dimensional space is that described in: [K. P. Bennett and O. L. Mangasarian: "Robust Linear Programming Discrimination of Two Linearly Inseparable Sets", Optimization Methods and Software 1, 1992, 23-34].
    \n
    This database is also available through the UW CS ftp server:
    ftp ftp.cs.wisc.edu
    cd math-prog/cpo-dataset/machine-learn/WDBC/
    \n
    Also can be found on UCI Machine Learning Repository: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

    Attribute Information:
    \n
    - Diagnosis (M = malignant, B = benign)
    3-32)
\n
    Ten real-valued features are computed for each cell nucleus:
\n
   \na) radius (mean of distances from center to points on the perimeter)
   \nb) texture (standard deviation of gray-scale values)
    \nc) perimeter
    \nd) area
    \ne) smoothness (local variation in radius lengths)
    \nf) compactness (perimeter^2 / area - 1.0)
    \ng) concavity (severity of concave portions of the contour)
    \nh) concave points (number of concave portions of the contour)
    \ni) symmetry
    \nj) fractal dimension ("coastline approximation" - 1)
\n
  \n  The mean, standard error and "worst" or largest (mean of the three
    largest values) of these features were computed for each image,
    resulting in 30 features. For instance, field 3 is Mean Radius, field
    13 is Radius SE, field 23 is Worst Radius.
    """,
    "disease": disease,
    "input_description": [
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
                                ],
    "scaler": Binary(breast_cancer_scaler_binary)
}


breast_cancer_gaussian_document = {
    "name": "breast_cancer_gpr",
    "disease": disease,
    "description": "breast_cancer_gpr is a gaussian process regressor trained with kaggle breast cancer wisconsin dataset https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data",
    "type": "gpr",
    "last_update": datetime.now(),
    "output_description": "the results may range from 0 to 1, where the closest to 0 means negative diagnosis and 1 is positive diagnosis",
    "model": Binary(breast_cancer_gaussian_binary),
}


result = models_collection.insert_one( breast_cancer_gaussian_document)
print(f"Model inserted with _id: {result.inserted_id}")

result = diseases_collection.insert_one( breast_cancer_disease_document)
print(f"Model inserted with _id: {result.inserted_id}")