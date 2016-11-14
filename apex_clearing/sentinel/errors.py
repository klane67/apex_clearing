from __future__ import unicode_literals


class APIError:
    def __init__(self, request):
        self.message = request.message
        self.code = request.status_code


class ServerError(APIError):
    pass


class BadRequestError(APIError):
    pass


class PermissionDeniedError(APIError):
    pass


class AuthError(APIError):
    pass


def error_from_response(r) -> APIError:
    code = r.status_code
    if code == 400:
        return BadRequestError(r)
    elif code == 401:
        return AuthError(r)
    elif code == 403:
        return PermissionDeniedError(r)
    elif code == 500:
        return ServerError(r)
    else:
        return APIError(r)
