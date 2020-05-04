from flask import Flask
from flask_restplus import Api

from tokengen import token_generator_v1
from tokengen import token_generator_v2
from .models.models import db
from . import config



def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    return flask_app


app = create_app()
api = Api(app=app, doc='/docs', version='1.0', title='Token Issuance API',
    description='Token Issuance Reference Implementation',)
#api.add_namespace(token_generator_v1.ns)
api.add_namespace(token_generator_v2.ns)


