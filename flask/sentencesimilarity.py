import requests
import string
import json
url = "https://twinword-text-similarity-v1.p.rapidapi.com/similarity/"

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

def computeSentenceSimilarity(question, usersaid):
	answers = questionToAnswer[question]
	maxSim = -999999
	usersaid.lower()
	for answer in answers:
		answer = answer.lower();
		maxSim = max(maxSim, private(answer, usersaid))
	return maxSim


question = "My dog died."

usersaid = "I'm sorry about what you are going through, and I want you to know that it will get better soon."
print(computeSentenceSimilarity(question, usersaid))