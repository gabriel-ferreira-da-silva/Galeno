from utils.commom_utils import *
from utils.database_utils import *
from flask import Blueprint, jsonify, request


general_blueprint = Blueprint('general_blueprint', __name__)


@general_blueprint.route("/diseases", methods=['GET'])
def heart_failure_predict_mlp():
    try:
        diseases = get_available_diseases()
        return jsonify(diseases)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    