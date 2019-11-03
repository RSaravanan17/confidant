import json

from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

from werkzeug.utils import secure_filename
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

import texttospeech
import speechtotext

import requests

app = Flask(__name__)
cors = CORS(app, resources={r"/v1/authenticate": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/health')
def index():
    return "I'm alive"

# @app.route('/v1/authenticate', methods=['POST'])
# @cross_origin(origin='*',headers=['Content-Type','Authorization'])
# def authenticate():
#     cred = credentials.Certificate("/etc/confidant/firebase-service-account.json")
#     firebase_admin.initialize_app(cred)

@app.route('/v1/speechToVid', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def speechToVid():
    try:
        data = request.args.to_dict()
    except ValueError:
        return jsonify({'error': "JSON data invalid or no input data"})

    # sanitization checks for input data
    if 'wavoutfilename' not in data or data['wavoutfilename'] is None or data['wavoutfilename'] == '':
        return jsonify({'error': "No output .wav file name specified"})

    if 'vidoutfilename' not in data or data['vidoutfilename'] is None or data['vidoutfilename'] == '':
        return jsonify({'error': "No output video file name specified"})

    wavinfilename = ''
    wavoutfilename = data['wavoutfilename']
    vidoutfilename = data['vidoutfilename']

    # check if the post request has the file part   
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file and allowed_file(file.filename):
        wavinfilename = secure_filename(file.filename)
        file.save(os.path.join('../public/audio/', wavinfilename, '.wav'))

    userText = speechtotext.speechToText('../public/audio/' + wavinfilename + '.wav')

    # somehow figure out what to say to the user
    responseText = ''
    texttospeech.textToSpeech(responseText, wavoutfilename)

    tf_model_fname = ''
    ds_fname = ''
    audio_fname = '../public/audio/' + wavoutfilename + '.wav'
    template_fname = ''
    condition_idx = ''
    out_path = '../public/video/' + vidoutfilename + '.mp4'
        
    inference(tf_model_fname, ds_fname, audio_fname, template_fname, condition_idx, out_path)

    return jsonify({'vidfilename': vidoutfilename, 'vidpath': '/public/audio/' + vidoutfilename})

@app.route('/v1/audioupload', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def audioupload():
    print("got upload request")
    if 'file' not in request.files:
        print('No file part')
        return ''
    file = request.files['file']
    if file.filename == '':
        print('No selected file')
        return ''
    if file:   
        filename = secure_filename(file.filename)
        filepath = os.path.join("../tempupload", "temp.wav")
        file.save(filepath)
    # Now, the file is saved in tempupload/filename
    result = speechtotext.speechToText(filepath)
    # judge the response
   
            
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