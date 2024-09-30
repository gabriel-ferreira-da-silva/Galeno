from classes.basemodel import basemodel
import numpy as np
from utils.database_utils import *
from utils.commom_utils import *


class heart_failure_mlp(basemodel):
    
    def __init__(self):
        super().__init__()
        self.name = "heart-failure-mlp"
    
    def format_results(self, prediction):
        results = {
                "disease": "heart failure",
                "model": "mlp",
                "modelname": "heart_failure_mlp",
                "result": prediction.tolist()
            }
        return results