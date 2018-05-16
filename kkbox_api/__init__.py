import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile(os.getcwd() + '/setting.cfg')

def setAppConfig(app, env):
    app.config[env] = os.environ.get(env, app.config[env])

setAppConfig(app, 'CLIENT_ID')
setAppConfig(app, 'CLIENT_SECRET')
setAppConfig(app, 'ALLOW_CORS_DOMAIN')

CORS(app, resources={"*": {"origins": app.config['ALLOW_CORS_DOMAIN']}})

from . import api
app.register_blueprint(api.bp, url_prefix='/')
