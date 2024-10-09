from classes.basemodel import basemodel
import numpy as np
from utils.database_utils import *
from utils.commom_utils import *


class heart_failure_kmedoid(basemodel):

    def __init__(self):
        super().__init__()
        self.name = "heart-failure-kmedoid"
        self.load()
