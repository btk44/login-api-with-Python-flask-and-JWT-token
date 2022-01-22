from flask_sqlalchemy import orm
from common.database import database


class RefreshTokenModel(database.Model):
    @orm.reconstructor
    def __init__(self):
        database.Model.__init__(self)

    @classmethod
    def create_for(cls, account_id, token_value, expiry_time):
        token = cls()
        token.token = token_value
        token.account_id = account_id
        token.expires_at = expiry_time

        return token

    __tablename__ = 'refresh_token'
    id = database.Column(database.Integer, unique=True, nullable=False, primary_key=True)
    token = database.Column(database.String(255), nullable=False)
    expires_at = database.Column(database.DateTime, nullable=False)
    account_id = database.Column(database.Integer, nullable=False)

