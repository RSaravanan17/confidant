import requests
import string
import json
url = "https://twinword-text-similarity-v1.p.rapidapi.com/similarity/"

currentQuestionId = 0
idToQuestion = dict()
idToQuestion[0] = "My dog died."

questionToId = dict()
questionToId["My dog died."] = 0

questionToAnswer = dict()
questionToAnswer["My dog died."] = ["I'm really sorry to hear that, it will get better soon.", "My deepest condolences, I empathize with you."]

headers = {
    'x-rapidapi-host': "twinword-text-similarity-v1.p.rapidapi.com",
    'x-rapidapi-key': "66707436f8mshde697637b6499e2p106547jsn2e624f4dd810"
    }

def private(text1, text2):
	querystring = {"text1": text1,"text2": text2}
	response = requests.request("GET", url, headers=headers, params=querystring)
	obj = json.loads(response.text)
	return obj['similarity']

def getNextQuestion(curQuestion):
	if(curQuestion == "0"): 
		currentQuestion = idToQuestion[0]
		currentQuestionId = 1
	else:
		currentQuestion = idToQuestion[currentQuestionId]
		currentQuestionId = currentQuestionId + 1
	return currentQuestion

def computeSentenceSimilarity(usersaid):
	answers = questionToAnswer[idToQuestion[currentQuestionId]]
	maxSim = -999999
	usersaid.lower()
	for answer in answers:
		answer = answer.lower();
		maxSim = max(maxSim, private(answer, usersaid))
	return maxSim


	