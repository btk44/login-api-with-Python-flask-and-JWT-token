from flask import Flask
from flask_cors import CORS
from common.app_settings import DATABASE_URI
from common.database import database
from auth.auth_controller import auth_api
from api.test_controller import test_api

app = Flask(__name__)

CORS(app)

# database setup
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
database.init_app(app)

# register all endpoints (buleprints) here
app.register_blueprint(auth_api)
app.register_blueprint(test_api)

# run application
if __name__ == '__main__': 
    app.debug = True
    app.run(host='0.0.0.0', port=4000)
