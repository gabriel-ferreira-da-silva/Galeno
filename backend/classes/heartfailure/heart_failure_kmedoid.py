from classes.basemodel import basemodel
import numpy as np
from utils.database_utils import *
from utils.commom_utils import *


class heart_failure_kmedoid(basemodel):

    def __init__(self):
        super().__init__()
        self.name = "heart-failure-kmedoid"
        self.load()

    def format_results(self, prediction):
        results = {
                "disease": "heart failure",
                "model": "kmedoid",
                "modelname": "heart_failure_kmedoid",
                "result": prediction.tolist()
            }
        return results
    
