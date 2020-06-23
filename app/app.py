from flask import Flask
from apiGatewayAPI import api_gateway_api

app = Flask(__name__)

app.register_blueprint(api_gateway_api)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()