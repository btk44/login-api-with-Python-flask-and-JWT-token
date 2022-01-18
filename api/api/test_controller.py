from flask import Blueprint
from flask import make_response
from auth.auth_service import AuthService

test_api = Blueprint('test_api', __name__, url_prefix='/test')


@test_api.route('/public', methods=['GET'])
def public_route():
    return make_response("Hello public", 200)


@test_api.route('/private', methods=['GET'])
@AuthService.authorize
def private_route():
    return make_response("Hello private", 200)
