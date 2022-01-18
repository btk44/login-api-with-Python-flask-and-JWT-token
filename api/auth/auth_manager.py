import datetime
from werkzeug.security import check_password_hash
from auth.account_model import AccountModel
from base.base_manager import BaseManager
from common.app_settings import REFRESH_TOKEN_EXPIRATION, TOKEN_EXPIRATION_CLAIM, TOKEN_EXPIRATION_TIME, TOKEN_ACCOUNT_CLAIM
from auth.token_service import TokenService


class AuthManager(BaseManager):
    def __init__(self):
        super(AuthManager, self).__init__()

    def login(self, account_name, password):
        account = AccountModel.query.filter_by(name=account_name).first()

        if not account or not check_password_hash(account.password, password):
            return self._get_error_result(None, 'Incorrect user or password', 401)

        token_expiration_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=TOKEN_EXPIRATION_TIME)
        token = TokenService.generate_token({
            TOKEN_ACCOUNT_CLAIM: 1,
            TOKEN_EXPIRATION_CLAIM: token_expiration_time
        })

        refresh_token = TokenService.generate_refresh_token()
        refresh_token_expiration_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=REFRESH_TOKEN_EXPIRATION)

        return self._get_ok_result({
            'token': token,
            'token_expiration_time': token_expiration_time,
            'refresh_token': refresh_token,
            'refresh_token_expiration_time': refresh_token_expiration_time
        })

    # def refresh_token(self, refresh_token_value):
    #     return self._get_ok_result(new_token_data)
