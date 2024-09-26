from .database_utils import *

def load_lung_cancer_mlp():
    lung_cancer_mlp = load_model("lung-cancer-mlp")
    return lung_cancer_mlp