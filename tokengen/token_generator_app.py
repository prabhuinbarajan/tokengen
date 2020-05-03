#!/usr/bin/env python
from flask import Flask
from flask_restful import Resource, Api
from tokengen.token_generator_v1 import TokenGeneratorV1

app = Flask(__name__)
api = Api(app)

api.add_resource(TokenGeneratorV1, '/v1/token/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
