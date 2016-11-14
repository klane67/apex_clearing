import requests

from .legit.auth import JWTAuth

__all__ = ['uat_login', 'prod_login', 'request']

settings = {
    'jwt_auth': None,  # type: JWTAuth
    'api_url': None,  # type: str
}


def uat_login(username, entity, shared_secret):
    api_url = 'https://uat-api.apexclearing.com/{}'
    settings['api_url'] = api_url
    settings['jwt_auth'] = JWTAuth(api_url, username, entity, shared_secret)


def prod_login(username, entity, shared_secret):
    api_url = 'https://api.apexclearing.com/{}'
    settings['api_url'] = api_url
    settings['jwt_auth'] = JWTAuth(api_url, username, entity, shared_secret)


def auth_request(*args, **kwargs):
    if 'auth' not in kwargs:
        kwargs['auth'] = settings['jwt_auth']
    return requests.request(*args, **kwargs)


def request(endpoint, method='get', json=None, params=None):
    url = settings['api_url'].format(endpoint)
    r = auth_request(method, url, params=params, json=json)
    if r.status_code == 401:
        jwt_auth = settings['jwt_auth']
        if jwt_auth.has_token:
            jwt_auth.reset()
            r = auth_request(method, url, params=params, json=json)
    return r
