import json
import string
import random
from hashlib import sha256

from sqlalchemy.ext.declarative import DeclarativeMeta


def alphanum_token_generator(base_length=5, checksum_length=0, remove_filter="", numeric_only=True):
    token_type = string.octdigits;
    if not numeric_only:
        token_type = token_type + string.ascii_letters;

    if remove_filter and len(remove_filter) > 0 :
        token_type=token_type.translate(str.maketrans('','', ''.join(remove_filter)))

    prefill = ''.join(random.choices(token_type, k=base_length))
    hashedWord = ''
    if(checksum_length > 0):
        hashedWord = sha256(prefill.encode('utf-8')).hexdigest()[-1*checksum_length:]

    result = prefill + hashedWord + '9'
    return result



class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)