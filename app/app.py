from flask import Flask
from apiGatewayAPI import api_gateway_api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(api_gateway_api)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, port=5010)
