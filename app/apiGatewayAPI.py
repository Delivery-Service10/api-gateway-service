from flask import Blueprint, request, jsonify, make_response
import requests
import json


api_gateway_api = Blueprint('api_gateway_api', __name__)


@api_gateway_api.route("/login/", methods=['POST'])
def login():
    data = request.get_json()

    r = requests.post('http://127.0.0.1:5001/login/', json=data)
    # print(r.text)
    return make_response(jsonify(data), 200)


@api_gateway_api.route("/create-account/", methods=['POST'])
def create_account():
    # Use the data variable and view it in the run instance when printed
    data = request.get_json()
    print(data)
    return make_response(jsonify(data), 200)

