import os
import requests
import time
from xml.etree import ElementTree

'''try:
    input = raw_input
except NameError:
    pass'''

class TextToSpeech(object):
    def __init__(self, subscription_key, actualText):
        self.subscription_key = subscription_key
        self.tts = actualText
        self.timestr = time.strftime("%Y%m%d-%H%M")
        self.access_token = None

    def get_token(self):
	    fetch_token_url = "https://southcentralus.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
	    #fetch_token_url = "https://westus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
	    headers = {
	        'Ocp-Apim-Subscription-Key': self.subscription_key
	    }
	    response = requests.post(fetch_token_url, headers=headers)
	    self.access_token = str(response.text)
    def save_audio(self):
	    base_url = 'https://southcentralus.tts.speech.microsoft.com/'
	    path = 'cognitiveservices/v1'
	    constructed_url = base_url + path
	    headers = {
	        'Authorization': 'Bearer ' + self.access_token,
	        'Content-Type': 'application/ssml+xml',
	        'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
	        'User-Agent': 'YOUR_RESOURCE_NAME'
	    }
	    xml_body = ElementTree.Element('speak', version='1.0')
	    xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
	    voice = ElementTree.SubElement(xml_body, 'voice')
	    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
	    voice.set(
	        'name', 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)')
	    voice.text = self.tts
	    body = ElementTree.tostring(xml_body)

	    response = requests.post(constructed_url, headers=headers, data=body)
	    if response.status_code == 200:
	        with open('sample-' + self.timestr + '.wav', 'wb') as audio:
	            audio.write(response.content)
	            print("\nStatus code: " + str(response.status_code) +
	                  "\nYour TTS is ready for playback.\n")
	    else:
	        print("\nStatus code: " + str(response.status_code) +
	              "\nSomething went wrong. Check your subscription key and headers.\n")


def textToSpeech(text):
    subscription_key = "9474dce2238e4429ac391b74f890e909"
    print ("hi")
    app = TextToSpeech(subscription_key, text)
    print ("hi2")
    app.get_token()
    print ("hi3")
    app.save_audio()

textToSpeech("l'hopital's")




