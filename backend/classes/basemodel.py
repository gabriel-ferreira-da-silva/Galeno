from abc import ABC, abstractmethod
from utils.database_utils import *
import numpy as np
from bson.binary import Binary
from datetime import datetime

class basemodel():

    def __init__(self):
        self.name = ""
        self.name = ""
        self.disease = ""
        self.type = ""
        self.last_update = ""
        self.input_description = []
        self.output_description = ""
        self.model =  None 
        self.scaler =  None

    @abstractmethod
    def get_header(self):
        header = {
                "modelname": self.name,
                "disease": self.disease,
                "model": self.type,
                "last_update":self.last_update,
                "input_description":self.input_description,
                "output_description":self.output_description,
            }
        return header
             
    @abstractmethod
    def load(self):
        model_object = get_model_object(self.name)
        self.name = model_object['name']
        self.disease = model_object['disease']
        self.type = model_object['disease']
        self.last_update = model_object['last_update']
        self.input_description = model_object['input_description']
        self.output_description = model_object['output_description']
        self.model =  model_object['model']
        self.scaler =  model_object['scaler']
    
    @abstractmethod
    def predict(self,input):
        input_array = np.array(input)
        prediction = self.model.predict(input_array.reshape(1, -1))
        return prediction
    
    @abstractmethod
    def format_results(self, prediction):
        results = {
                "disease": self.disease,
                "model": self.type,
                "modelname": self.name,
                "result": prediction.tolist()
            }
        return results
 
    @abstractmethod
    def get_formated_input(self, data):
        input_array = data['input_array']
        input = self.scale_input(input_array)
        return input
    
    @abstractmethod
    def scale_input(self, input):
        input_array = np.array(input)
        input_array = input_array.reshape(1,-1)
        input = self.scaler.transform(input_array)
        return input

    

    @abstractmethod
    def get_results(self, data):
        
        input = self.get_formated_input(data)
        prediction = self.predict(input)
        results = self.format_results(prediction)
        return results
        

    @abstractmethod
    def train(self, data):
        training_data = data['training_data']
        
        X = []
        y = []

        for arr in training_data:
            X_features = arr[:-1]  
            label = arr[-1]  

            X_scaled = self.scale_input(X_features)

            X.append(X_scaled)
            y.append(label)

        X = np.array(X).reshape(len(X), -1)  
        y = np.array(y)

        self.model.fit(X, y)

        models_collection = load_models()
        model_binary = pickle.dumps(self.model)
        models_collection.update_one(
            {"name": self.name},
            {"$set": {"model": Binary(model_binary), "last_update": datetime.now()}}
        )