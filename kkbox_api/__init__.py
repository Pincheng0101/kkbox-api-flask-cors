import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile(os.getcwd() + '/setting.cfg')

CORS(app, resources={"*": {"origins": app.config['ALLOW_CORS_DOMAIN']}})

from . import api
app.register_blueprint(api.bp, url_prefix='/')
