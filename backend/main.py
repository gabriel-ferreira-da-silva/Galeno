from flask import Flask
from flask import Flask
from flask_cors import CORS
from server.diseasesServer import diseases_blueprint
from server.modelsServer import models_blueprint


app = Flask(__name__)
CORS(app)

app.register_blueprint(diseases_blueprint, url_prefix='/api')
app.register_blueprint(models_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
