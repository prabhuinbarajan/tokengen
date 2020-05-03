from flask import Flask
from flask_restplus import Api

from tokengen.token_generator_v1 import token_ns_v1
from tokengen.token_generator_v2 import token_ns_v2
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
api = Api(app=app, doc='/docs')
api.add_namespace(token_ns_v1)
api.add_namespace(token_ns_v2)


