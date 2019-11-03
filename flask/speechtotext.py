import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
class SpeechToText():
	def __init__(self, key, filename):
		self.key = key
		self.region = "southcentralus"
		self.filename = filename

		speech_key, service_region = self.key, "southcentralus"
		self.speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

		# Creates a recognizer with the given settings
		self.audio_config = speechsdk.audio.AudioConfig(filename=self.filename)

	def getTextFromSpeech(self):
		speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config, audio_config=self.audio_config)

		print("started trying to understand...")


		# Starts speech recognition, and returns after a single utterance is recognized. The end of a
		# single utterance is determined by listening for silence at the end or until a maximum of 15
		# seconds of audio is processed.  The task returns the recognition text as result. 
		# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
		# shot recognition like command or query. 
		# For long-running multi-utterance recognition, use start_continuous_recognition() instead.
		result = speech_recognizer.recognize_once()
		print (type(result))
		# Checks result.
		if result.reason == speechsdk.ResultReason.RecognizedSpeech:
			print("Recognized: {}".format(result.text))
			return result.text
		elif result.reason == speechsdk.ResultReason.NoMatch:
			print("No speech could be recognized: {}".format(result.no_match_details))
		elif result.reason == speechsdk.ResultReason.Canceled:
			cancellation_details = result.cancellation_details
			print("Speech Recognition canceled: {}".format(cancellation_details.reason))
			if cancellation_details.reason == speechsdk.CancellationReason.Error:
				print("Error details: {}".format(cancellation_details.error_details))
		return " "
 

def speechToText(fn):
	stt = SpeechToText("9474dce2238e4429ac391b74f890e909", fn)
	res = stt.getTextFromSpeech()
	return res
	# TODO: return text

speechToText("sample-20191102-1402.wav")





