from nltk.tokenize import word_tokenize
import random
import torch
import json
import os

from nltk_utils import bag_of_words, tokenize
from model import NeuralNet
from functions import *


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

files = ["daily.json", "func.json"]

cur_path = os.path.dirname(__file__)
intents = []
for i in files: 
    with open(os.path.relpath(f'.\\intents\\{i}', cur_path), 'r') as f:
        intents.extend(json.load(f))


FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
Ids = data['Ids']
model_state = data["model_state"]
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

question_words = ["what", "why", "when", "where", "is", "how", "do", "does", "which", "are", "could", "would", "should", "has", "have", "whom", "whose", "who"]



Aname = 'EDITH'
Oname = {"name": "amir m.", "type": "person"}#person/family
timezoneapikey = "acDmknoIUzJkoUZYemqS"


def res(Message, Ip, UserId):
    # mycursor.execute(f"SELECT * FROM i where sen = '{Message.lower()}'")

    # res = mycursor.fetchall()


    # print(res)

    sentence = tokenize(Message)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    Id = Ids[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.99:

        for intent in intents:
            if Id == intent["Id"]:
                res = random.choice(intent['responses'])

                if len(res["SFunction"]) > 0:

                    return json.dumps(globals()[res["SFunction"]](Message, Ip, UserId))
                    # return json.dumps(eval(res["SRunCode"]))

                return json.dumps(res)
    else:
        ferzan = Message.lower()
        ferzan = word_tokenize(ferzan)

        if any(x in ferzan[0] for x in question_words):
            return "{ \"commend\": \"Here are some search results.\", \"SFunction\": \"\", \"CFunction\": \"OpenUrl\", \"CFunctionPrams\": {\"url\":" + f"\"https://www.google.com/search?q={Message}\"" + "} }"
        return "{\"commend\": \"I coulden't underestand that\",\"SFunction\": \"\",\"CFunction\": \"\",\"CFunctionPrams\": {} }"