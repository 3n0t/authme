# -*- coding: utf-8 -*-

__all__ = ['authme', 'DEFAULT_TOKEN_HEAD', 'DEFAULT_TOKEN_LEN']

import re
import hashlib
import base64

DEFAULT_TOKEN_HEAD = 'aU0?'
DEFAULT_TOKEN_LEN = 20


def authme(domain, login, key, token_head=DEFAULT_TOKEN_HEAD, token_len=DEFAULT_TOKEN_LEN):
    """
    return domain-level auth token

    """
    assert isinstance(domain, basestring)
    assert isinstance(login, basestring)
    assert isinstance(key, basestring)
    assert isinstance(token_head, basestring)
    assert isinstance(token_len, int)
    domain, login, key, token_head = map(lambda v: str(v).strip(),
        (domain, login, key, token_head))
    assert domain and login and key, 'domain & login & key must be specified'
    head_len = len(token_head)
    body_len = token_len - head_len
    assert body_len > 0, 'token_len must be > %s' % head_len
    dl = domain + '\0' + login
    dk = hashlib.pbkdf2_hmac('sha256', dl, key, 10**5, dklen=body_len)
    b64 = base64.b64encode(dk)
    token_body = re.sub(r'[^a-zA-Z0-9]', '', b64)[:body_len]
    assert token_body
    token = token_head + token_body
    return token
