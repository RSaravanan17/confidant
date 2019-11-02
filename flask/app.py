import json

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

import requests

app = Flask(__name__)
cors = CORS(app, resources={r"/v1/authenticate": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/health')
def index():
    return "I'm alive"

@app.route('/v1/authenticate', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def authenticate():
    cred = credentials.Certificate("/etc/confidant/firebase-service-account.json")
    firebase_admin.initialize_app(cred)


@app.route('/v1/blahblah', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def blahblah():
    try:
        data = request.args.to_dict()
    except ValueError:
        return jsonify({'error': "JSON data invalid or no input data"})

    # sanitization checks for email and client IP data
    if 'email' not in data or data['email'] is None or data['email'] == '':
        return jsonify({'error': "No email specified"})

    if 'clientIp' not in data or data['clientIp'] is None or data['clientIp'] == '':
        return jsonify({'error': "No client IP specified"})

    # prepare for Shopper API call
    clean_data = {"auditClientIp": data['clientIp'], "email": data['email']}
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Access-Control-Allow-Credentials': 'true'}
    cert = (ssl_crt_path, ssl_key_path)
    headers['Authorization'] = 'sso-jwt ' + _get_jwt(cert)

    print(clean_data)

    # send request to Shopper API
    response = requests.get(api_endpoint, params=clean_data, headers=headers)
    json_response = response.json()

    # add checks for unexpected JSON response

    # return API response
    return_response = {'exists': False}
    if (len(json_response) > 0):
        # no duplicate email
        return_response['exists'] = True
    return jsonify(return_response)


def _get_jwt(cert):
    """
    Attempt to retrieve the JWT associated with the cert/key pair from SSO
    :param cert:
    :return:
    From: https://godaddy.slack.com/archives/C02Q2MEH8/p1564512016073700
    """
    try:
        response = requests.post(sso_endpoint, data={'realm': 'cert'}, cert=cert)
        response.raise_for_status()

        body = json.loads(response.text)
        return body.get('data')  # {'type': 'signed-jwt', 'id': 'XXX', 'code': 1, 'message': 'Success', 'data': JWT}
    except Exception as e:
        print(e.message)
    return None
