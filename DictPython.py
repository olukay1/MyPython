import json
data = json.load(open("data.json"))

def retrieveDefinition(word):
    return data [word]
#Get input from user
word_user = input("Enter a word: ")

print(retrieveDefinition(word_user))