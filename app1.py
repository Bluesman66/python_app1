import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        match = get_close_matches(word, data.keys())
        if len(match) > 0:
            return "did you mean \'{}\' instead?".format(match[0])
        else:
            return "The word {} does not exist. Please double check it."

word = input("Enter the world: ")

print(translate(word))
