#!/usr/bin/env python
import json
import uuid
from datetime import datetime, timedelta
from distutils.util import strtobool

from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields,reqparse
from tokengen.models.models import tokens
from tokengen.utils import alphanum_token_generator, AlchemyEncoder

ns = Namespace('v2/tokens', description='Token operations')

parser = reqparse.RequestParser()


token_model = ns.model('Token', {
    'id': fields.String(description='Token Id'),
    'token': fields.String(description='Upload Token'),
    'crypto_key': fields.String(description='Upload Key'),
    'key_status': fields.String(description='key status'),
    'key_expiry': fields.String(description='Upload Key Expiration Date'),
    'created_date': fields.DateTime(description='Token created date'),
    'updated_at': fields.DateTime(description='Token updated date')
});

@ns.route('/')
class TokenV2List(Resource):
    '''lets you generate new tokens'''
    @ns.marshal_list_with(token_model)
    @ns.doc(
        description="dry run of token without DB store",
        responses={
            201: 'Success',
            400: 'Validation Error'
        }
    )
    @ns.param('token_length', 'length of the token', type='int', default=5)
    @ns.param('checksum_length', 'length of checksum', type='int', default=1)
    @ns.param('remove_filter', description='characters to be not used in token generation - default token is made \
        of [0-7,a-z,A-Z]. remove list should be a subset of these', default=' ')
    @ns.param('numeric_only', description='numeric only', type='boolean', default=True)
    @ns.expect(validate=True)
    def get(self ):
        '''dry run'''
        base_length = int(request.args.get('token_length'))
        checksum_length = int(request.args.get('checksum_length'))
        remove_filter = request.args.get('remove_filter')
        numeric_only = strtobool(request.args.get('numeric_only'))


        key = str(uuid.uuid4());
        upload_token = alphanum_token_generator(base_length=base_length, checksum_length=checksum_length,
                                                remove_filter=remove_filter, numeric_only=numeric_only);

        token = tokens(id=key, token=upload_token, crypto_key=key, key_status="unverified",
                       created_date=datetime.utcnow(), updated_at=datetime.utcnow(),
                       key_expiry=datetime.utcnow() + timedelta(days=14))
        #json_res = json.dumps(token, cls=AlchemyEncoder)
        return token, 200
        # database.add_instance(tokens,id=key, )


    '''lets you generate new tokens'''
    @ns.doc('request a token')
    @ns.marshal_list_with(token_model)
    @ns.doc(
        description="issue a token",
        responses={
            201: 'Success',
            400: 'Validation Error'
        }
    )
    def post(self):
        '''issue a proper token'''
        data = request.get_json()
        key = uuid.uuid4();
        upload_token = alphanum_token_generator()
        #database.add_instance(tokens,id=key, )


@ns.route('/<id>')
@ns.param('id', 'The token identifier')
class TokenV2(Resource):
    def get(self):
        '''get token by id'''
        return {'token': self.generate_token("visa16"), "key": "hashashashashas"}

    def generate_token(self, type):
        """
        Prefill some values based on the card type
        """
        return "123";
