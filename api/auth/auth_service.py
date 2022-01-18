from functools import wraps
from flask import request, make_response, g
from auth.token_service import TokenService
from auth.auth_constants import TOKEN_HEADER_NAME


class AuthService:
    @staticmethod
    def authorize(f):
        @wraps(f)
        def auth_verifier(*args, **kwargs):
            token = None

            if TOKEN_HEADER_NAME in request.headers:
                token = request.headers[TOKEN_HEADER_NAME]

            if not token:
                return make_response('Token is missing', 401)

            token_claims = TokenService.get_token_claims(token)

            if not token_claims:
                return make_response('Token is invalid', 401)

            g.token = token_claims

            return f(*args, **kwargs)

        return auth_verifier
