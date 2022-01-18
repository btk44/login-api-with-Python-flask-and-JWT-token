from flask_sqlalchemy import orm
from common.database import database


class AccountModel(database.Model):
    @orm.reconstructor
    def __init__(self):
        database.Model.__init__(self)

    __tablename__ = 'account'
    id = database.Column(database.Integer, unique=True, nullable=False, primary_key=True)
    name = database.Column(database.String(500),  unique=True, nullable=False)
    password = database.Column(database.String(500), nullable=False)

