from classes.basemodel import basemodel
import numpy as np
from utils.database_utils import *
from utils.commom_utils import *


class breast_cancer_gpr(basemodel):
    
    def __init__(self):
        super().__init__()
        self.name = "breast_cancer_gpr"
        self.load()