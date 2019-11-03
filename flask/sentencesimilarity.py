import requests
import string
import json

import random
url = "https://twinword-text-similarity-v1.p.rapidapi.com/similarity/"

currentQuestionId = 0
idToQuestion = ["My dog died. ", "I really miss my dog. His name was Buddy.", "I hope Buddy is happy, wherever he is."]
goodResponses = ["Thanks for understanding, ", "I'm grateful that you get it, ", "You're a good listener, "]
badResponses = ["You're so rude, ", "Why would you say that? " , "Don't be so mean, "]

questionToAnswer = [[], [], []]
questionToAnswer[0] = ["I'm really sorry to hear that, it will get better soon.", "My deepest condolences, I empathize with you."]
questionToAnswer[1] = ["It's okay to miss loved ones. ", "I miss him too", "I'm sure Buddy misses you too."]

headers = {
    'x-rapidapi-host': "twinword-text-similarity-v1.p.rapidapi.com",
    'x-rapidapi-key': "66707436f8mshde697637b6499e2p106547jsn2e624f4dd810"
    }

def private(text1, text2):
	querystring = {"text1": text1,"text2": text2}
	response = requests.request("GET", url, headers=headers, params=querystring)
	obj = json.loads(response.text)
	return obj['similarity']

def getNextResponse(score):
	emoResponse = ""
	if score > 0.35: 
		emoResponse = goodResponses[random.randint(0, len(goodResponses)-1)]
	else:
		emoResponse = badResponses[random.randint(0, len(badResponses)-1)]
	global currentQuestionId
	currentQuestionId = currentQuestionId + 1
	return emoResponse + getQuestion(currentQuestionId)

def getFirstQuestion():
	currentQuestionId = 0
	return idToQuestion[0]

def getQuestion(id):
	if(id > len(idToQuestion)):
		return ""
	currentQuestion = idToQuestion[id]
	return currentQuestion

def computeSentenceSimilarity(usersaid):
	global currentQuestionId
	global questionToAnswer
	answers = questionToAnswer[currentQuestionId]
	maxSim = -999999
	usersaid.lower()
	for answer in answers:
		answer = answer.lower();
		maxSim = max(maxSim, private(answer, usersaid))
	return maxSim


	