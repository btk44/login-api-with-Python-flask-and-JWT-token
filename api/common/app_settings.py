# auth
TOKEN_SECRET_KEY = 'w5L39htO1nBJyH8mgaAVQcUmZZdZkjetMlYh6k8Wvsd16K_ob0B4Y'
TOKEN_ALGORITHM = 'HS256'
TOKEN_EXPIRATION_TIME = 3600
REFRESH_TOKEN_EXPIRATION = TOKEN_EXPIRATION_TIME * 2
REFRESH_TOKEN_LENGTH = 64
TOKEN_ACCOUNT_CLAIM = 'account'
TOKEN_EXPIRATION_CLAIM = 'exp'

# db
DATABASE_URI = 'mysql://admin:admin@localhost/loginappdb'
