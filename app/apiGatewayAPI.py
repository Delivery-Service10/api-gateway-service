import requests
import json
import jwt
import datetime
from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin

api_gateway_api = Blueprint('api_gateway_api', __name__)


@api_gateway_api.route("/test/", methods=['POST'])
@cross_origin(supports_credentials=True)
def test():
    if 'token' in request.cookies:
        data = request.cookies.get("token")
        print(data)
    else:
        print('not found')
    return make_response(jsonify({'message':'xD'}))


@api_gateway_api.route("/login/", methods=['POST'])
@cross_origin(supports_credentials=True)
def login():
    data = request.get_json()

    r = requests.post('http://127.0.0.1:5001/login/', json=data)
    if r.status_code == 200:
        public_id = json.loads(r.text)[0]['public_id']
        name = json.loads(r.text)[0]['Name']
        token = encode_auth_token(public_id)
        response_obj = {
            'status': 'success',
            'message': 'Logged in successfully',
            'Name': name
        }
        response = make_response(jsonify(response_obj))
        response.set_cookie('token',
                            token.decode(),
                            httponly=True,
                            # domain='127.0.0.1 localhost dev.localhost',
                            # secure=True,
                            max_age=60 * 60)
        return response, 200

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
    # data = request.get_json()
    data = {'first_name': 'First', 'last_name': 'Last', 'email': 'udc2@gmail.com', 'password': 'random'}
    print(data)
    return make_response(jsonify(data), 200)

