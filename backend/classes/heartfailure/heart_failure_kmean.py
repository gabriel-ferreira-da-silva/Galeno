from classes.basemodel import basemodel
import numpy as np
from utils.database_utils import *
from utils.commom_utils import *


class heart_failure_kmean(basemodel):

    def __init__(self):
        super().__init__()
        self.name = "heart-failure-kmean"

    def load(self):
        heart_failure_mlp = load_model("heart-failure-kmean")
        return heart_failure_mlp
    
    def predict(self,input):
        input_array = np.array(input)
        heart_failure_mlp = self.load()
        prediction = heart_failure_mlp.predict(input_array.reshape(1, -1))
        return prediction
    
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
