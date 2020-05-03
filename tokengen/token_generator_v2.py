#!/usr/bin/env python
from flask_restful import Resource

class TokenGeneratorV2(Resource):
    def get(self):
        return {'token': self.generate_card("visa16"), "key": "hashashashashas"}

    def generate_token(self, type):
        """
        Prefill some values based on the card type
        """
        return "123";
