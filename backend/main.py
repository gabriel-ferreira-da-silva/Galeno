from flask import Flask
from server.generalServer import general_blueprint
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.register_blueprint(general_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
