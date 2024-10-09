from classes.basemodel import basemodel
import numpy as np
from utils.database_utils import *
from utils.commom_utils import *


class lung_cancer_mlp(basemodel):
    
    def __init__(self):
        super().__init__()
        self.name = "lung-cancer-mlp"
        self.load()