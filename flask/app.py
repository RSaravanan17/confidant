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
    
import subprocess
import sentencesimilarity
import requests

app = Flask(__name__)
cors = CORS(app, resources={r"/v1/authenticate": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

currentQ = '';

@app.route('/health')
def index():
    return "I'm alive"

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    proc_stderr = process.communicate()[1].strip();
    print(proc_stderr)
    print(proc_stdout)


@app.route('/v1/firstQ', methods=['POST'])
def firstQ():
    print("TEST")
    q = sentencesimilarity.getNextQuestion("0")
    print("Q:  " + q)
    textToVid(q, "../tempupload/botwav.wav")
    return ""

    

# @app.route('/v1/authenticate', methods=['POST'])
# @cross_origin(origin='*',headers=['Content-Type','Authorization'])
# def authenticate():
#     cred = credentials.Certificate("/etc/confidant/firebase-service-account.json")
#     firebase_admin.initialize_app(cred)



def textToVid(text, wavinfilename):
    texttospeech.textToSpeech(text, wavinfilename)


    # check if the post request has the file part   

    tf_model_fname = '../voca/model/gstep_52280.model'
    ds_fname = '../voca/ds_graph/output_graph.pb'
    audio_fname = wavinfilename
    template_fname = '../voca/template/FLAME_sample.ply'
    condition_idx = '3'
    
    subprocess_cmd('echo a; cd ../voca; rm -rf ./animation_output/*; rm -rf ../public/video.mp4; ' +
    'python run_voca.py --tf_model_fname ./model/gstep_52280.model --ds_fname ./ds_graph/output_graph.pb --audio_fname ' + wavinfilename + ' --template_fname ./template/FLAME_sample.ply --condition_idx 3 --out_path ./animation_output;' + 
    'python visualize_sequence.py --sequence_path \'animation_output/\' --audio_fname \'' + wavinfilename + '\' --out_path \'../public\';'
    )

@app.route('/v1/audioupload', methods=['GET', 'POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def audioupload():
    print("got upload request")
    filepath = ''
    if 'file' not in request.files:
        print('No file part')
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    if file.filename == '':
        print('No selected file')
        return jsonify({'error': 'No selected file'})
    if file:   
        filename = secure_filename(file.filename)
        filepath = os.path.join("../tempupload", "temp.wav")
        file.save(filepath)
    # Now, the file is saved in tempupload/filename
    userResult = speechtotext.speechToText(filepath)
    userText = userResult;

    similarity = sentencesimilarity.computeSentenceSimilarity(userText)
    print(similarity);
    return jsonify({'score' : similarity})
            
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