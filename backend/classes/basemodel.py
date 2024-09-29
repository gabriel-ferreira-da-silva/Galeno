from abc import ABC, abstractmethod
from utils.database_utils import *
import numpy as np

class basemodel():

    def __init__(self):
        self.name = ""

    @abstractmethod
    def get_header(self):
        pass

    def load(self):
        model = load_model(self.name)
        return model
    
    def predict(self,input):
        input_array = np.array(input)
        model = self.load()
        prediction = model.predict(input_array.reshape(1, -1))
        return prediction
    

    @abstractmethod
    def format_results(self):
        pass

    @abstractmethod
    def get_results(self):
        pass
