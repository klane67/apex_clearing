from __future__ import unicode_literals

import json
from datetime import datetime

import base64
import jws
import requests
from requests.auth import AuthBase


class JWTAuth(AuthBase):
    __jwt = None

    def __init__(self, api_url, username, entity, shared_secret):
        self.api_url = api_url
        self.username = username
        self.entity = entity
        self.shared_secret = shared_secret

    @property
    def has_token(self):
        return self.__jwt is not None

    def reset(self):
        self.__jwt = None

    def _login(self):
        def to_base64(s):
            return base64.urlsafe_b64encode(s).replace('=', '')

        header = {'alg': 'HS512'}
        body = {
            'username': self.username,
            'entity': self.entity,
            'datetime': datetime.utcnow().isoformat('T')
        }
        signature = jws.sign(header, body, self.shared_secret)

        encoded_header = to_base64(json.dumps(header))
        encoded_body = to_base64(json.dumps(body))
        # signature is already encoded

        r = requests.get(self.api_url.format('/v1/cc/token'), params={
            'jws': '%s.%s.%s' % (encoded_header, encoded_body, signature),
        })
        if r.status_code == 200:
            return r.content

    def __call__(self, r):
        if self.__jwt is None:
            jwt = self._login()
            if jwt:
                r.headers['Authorization'] = 'Authorization: %s' % jwt
                self.__jwt = jwt
        return r
