from flask import Flask
from server.lungCancerServer import lungCancerModel_blueprint
from server.heartDiseaseServer import heart_failure_model_blueprint
app = Flask(__name__)

app.register_blueprint(lungCancerModel_blueprint, url_prefix='/api')
app.register_blueprint(heart_failure_model_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
