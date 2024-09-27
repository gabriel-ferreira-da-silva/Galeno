from .database_utils import *

def load_heart_failure_mlp():
    heart_failure_mlp = load_model("heart-failure-mlp")
    return heart_failure_mlp