import requests
import string
import json
import math

import random
url = "https://twinword-text-similarity-v1.p.rapidapi.com/similarity/"

currentQuestionId = 0
idToQuestion = ["My dog died. ", "I really miss my dog. His name was Buddy.", "I hope Buddy is happy, wherever he is.", "I got promoted at work!", "I am getting married!", "My girlfriend broke up with me."]
goodResponses = ["Thanks for understanding, ", "I'm grateful that you get it, ", "You're a good listener, "]
badResponses = ["You're so rude, ", "Why would you say that? " , "Don't be so mean, "]

questionToAnswer = list()
questionToAnswer.append(["I'm really sorry to hear that, it will get better soon.", "My deepest condolences, I empathize with you."])
questionToAnswer.append(["It's okay to miss loved ones. ", "I miss him too", "I'm sure Buddy misses you too."])
questionToAnswer.append(["May he rest in peace in heaven.", "I am sure he is happy too.", "He is happy in paradise."])
questionToAnswer.append(["That's great to hear!", "Super cool! Keep it up!", "You did a great job!"])
questionToAnswer.append(["Wow you are so lucky!", "Wishing you a happy and loving life!", "Congratulations on the engagement!"])
questionToAnswer.append(["I'm so sorry.", "You will get through this, don't worry.", "You are better off without her, you are an amazing."])

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
	if score > 0.25: 
		emoResponse = goodResponses[random.randint(0, len(goodResponses)-1)]
	else:
		emoResponse = badResponses[random.randint(0, len(badResponses)-1)]
	global currentQuestionId
	currentQuestionId = (currentQuestionId + 1) % len(questionToAnswer)
	return emoResponse + getQuestion(currentQuestionId)

def getFirstQuestion():
	global startIndex
	currentQuestionId = random.randint(0, len(questionToAnswer)-1)
	startIndex = currentQuestionId
	return idToQuestion[currentQuestionId] #dont call getQuestion here, keep it as idToQuestion[currentQuestionId]

def getQuestion(id):
	global startIndex
	if(id == startIndex):
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


	