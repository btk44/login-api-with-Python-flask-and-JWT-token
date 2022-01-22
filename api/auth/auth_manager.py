import datetime
from werkzeug.security import check_password_hash
from auth.models.account_model import AccountModel
from auth.models.refresh_token_model import RefreshTokenModel
from base.base_manager import BaseManager
from common.app_settings import REFRESH_TOKEN_EXPIRATION, TOKEN_EXPIRATION_CLAIM, TOKEN_EXPIRATION_TIME, TOKEN_ACCOUNT_CLAIM
from auth.token_service import TokenService
from common.database import database


class AuthManager(BaseManager):
    def __init__(self):
        super(AuthManager, self).__init__()

    def login(self, account_name, password):
        account = AccountModel.query.filter_by(name=account_name).first()

        if not account or not check_password_hash(account.password, password):
            return self._get_error_result(None, 'Incorrect user or password', 401)

        token, token_expiration_time, refresh_token = self.generate_token_data(account)

        # can be replaced with db trigger
        now = datetime.datetime.utcnow()
        RefreshTokenModel.query.filter(RefreshTokenModel.account_id == account.id,
                                       RefreshTokenModel.expires_at < now).delete()

        database.session.add(refresh_token)
        database.session.commit()

        return self._get_ok_result({
            'token': token,
            'token_expiration_time': token_expiration_time,
            'refresh_token': refresh_token.token,
            'refresh_token_expiration_time': refresh_token.expires_at
        })

    def refresh_token(self, account_id, refresh_token_value):
        old_refresh_token = RefreshTokenModel.query.filter_by(account_id=account_id,
                                                              token=refresh_token_value).first()

        account = AccountModel.query.filter_by(id=account_id).first()

        if not old_refresh_token or not account:
            return self._get_error_result(None, 'Invalid refresh token', 400)

        token, token_expiration_time, new_refresh_token = self.generate_token_data(account)

        database.session.delete(old_refresh_token)
        database.session.add(new_refresh_token)
        database.session.commit()

        return self._get_ok_result({
            'token': token,
            'token_expiration_time': token_expiration_time,
            'refresh_token': new_refresh_token.token,
            'refresh_token_expiration_time': new_refresh_token.expires_at
        })

    def generate_token_data(self, account):
        token_expiration_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=TOKEN_EXPIRATION_TIME)
        token = TokenService.generate_token({
            TOKEN_ACCOUNT_CLAIM: 1,
            TOKEN_EXPIRATION_CLAIM: token_expiration_time
        })

        refresh_token = RefreshTokenModel\
            .create_for(account.id,
                        TokenService.generate_refresh_token(),
                        datetime.datetime.utcnow() + datetime.timedelta(seconds=REFRESH_TOKEN_EXPIRATION))

        return token, token_expiration_time, refresh_token
