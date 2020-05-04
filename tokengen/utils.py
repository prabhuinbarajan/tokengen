import string
import random
from hashlib import sha256


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
