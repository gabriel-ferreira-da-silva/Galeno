from classes.basemodel import basemodel
import numpy as np
from utils.database_utils import *
from utils.commom_utils import *


class heart_failure_kmean(basemodel):

    def __init__(self):
        super().__init__()
        self.name = "heart-failure-kmean"
    
    def format_results(self, prediction):
        results = {
                "disease": "heart failure",
                "model": "kmean",
                "modelname": "heart_failure_kmean",
                "result": prediction.tolist()
            }
        return results
    
    def get_results(self, data):
        input = data['input_array']
        prediction = self.predict(input)
        results = self.format_results(prediction)
        return results
