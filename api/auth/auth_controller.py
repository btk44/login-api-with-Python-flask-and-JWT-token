from flask import Blueprint
from flask import request, jsonify, make_response
from auth.dto.account_dto import AccountDto
from auth.auth_manager import AuthManager

auth_api = Blueprint('auth_api', __name__, url_prefix='/auth')


@auth_api.route('/login', methods=['POST'])
def login():
    account_dto = AccountDto.from_json(request.get_json())
    success, token_data, message, status_code = AuthManager().login(account_dto.account_name, account_dto.password)

    if not success:
        return make_response(message, status_code)

    return make_response(jsonify(token_data), 200)


@auth_api.route('/refresh', methods=['POST'])
def refresh():
    data = request.get_json()

    if not data or not data['refreshToken'] or not data['accountId']:
        return make_response('Missing data', 400)

    auth_manager = AuthManager()
    success, token_data, message, status_code = auth_manager.refresh_token(data['accountId'], data['refreshToken'])

    if not success:
        return make_response(message, status_code)

    return jsonify(token_data)
