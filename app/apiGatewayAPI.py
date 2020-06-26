import requests
import json
import jwt
import datetime
from flask import Blueprint, request, jsonify, make_response

api_gateway_api = Blueprint('api_gateway_api', __name__)


@api_gateway_api.route("/login/", methods=['POST'])
def login():
    data = request.get_json()

    r = requests.post('http://127.0.0.1:5001/login/', json=data)
    if r.status_code == 200:
        public_id = json.loads(r.text)[0]['public_id']
        token = encode_auth_token(public_id)
        response_obj = {
            'status': 'success',
            'message': 'Logged in successfully',
            'auth_token': token.decode()
        }
        return make_response(jsonify(response_obj), 200)

    else:
        response_obj = {
            'status': 'success',
            'message': 'Logged in successfully'
        }
    return make_response(jsonify(response_obj), r.status_code)


def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            'ThisIsSecretKey',
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, 'ThisIsSecretKey')
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


@api_gateway_api.route("/create-account/", methods=['POST'])
def create_account():
    # Use the data variable and view it in the run instance when printed
    data = request.get_json()
    print(data)
    return make_response(jsonify(data), 200)

