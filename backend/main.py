from flask import Flask
from server.generalServer import general_blueprint
from server.lungCancerServer import lungCancerModel_blueprint
from server.heartDiseaseServer import heart_failure_model_blueprint
from server.breastCancerServer import breast_cancer_model_blueprint
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.register_blueprint(general_blueprint, url_prefix='/api')
app.register_blueprint(lungCancerModel_blueprint, url_prefix='/api')
app.register_blueprint(heart_failure_model_blueprint, url_prefix='/api')
app.register_blueprint(breast_cancer_model_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
