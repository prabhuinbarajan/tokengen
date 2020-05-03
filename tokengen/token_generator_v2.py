#!/usr/bin/env python
from flask_restplus import Resource, Namespace

token_ns_v2 = Namespace('tokens', description='Token operations')

@token_ns_v2.route('/v2/token')
class TokenGeneratorV2(Resource):
    def get(self):
        return {'token': self.generate_token("visa16"), "key": "hashashashashas"}

    def generate_token(self, type):
        """
        Prefill some values based on the card type
        """
        return "123";
