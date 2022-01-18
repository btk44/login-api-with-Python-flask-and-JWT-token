import re
import string
import random
import jwt
from common.app_settings import TOKEN_ALGORITHM, TOKEN_SECRET_KEY, REFRESH_TOKEN_LENGTH
from auth.auth_constants import TOKEN_HEADER_REGEX, TOKEN_REGEX


class TokenService:
    @staticmethod
    def get_token_claims(token):
        if not re.match(TOKEN_HEADER_REGEX, token):
            return False

        try:
            token = re.search(TOKEN_REGEX, token).group(0)
            token_data = jwt.decode(token, TOKEN_SECRET_KEY)

            return token_data
        except jwt.exceptions.InvalidTokenError:
            return False

    @staticmethod
    def generate_token(claims_dict):
        if type(claims_dict) is not dict:
            return False

        token = jwt.encode(
            claims_dict,
            TOKEN_SECRET_KEY,
            algorithm=TOKEN_ALGORITHM)

        return token

    @staticmethod
    def generate_refresh_token():
        letters = string.ascii_letters + '1234567890!@#$%^&*()_-+=?>'
        return ''.join(random.choice(letters) for i in range(REFRESH_TOKEN_LENGTH))

