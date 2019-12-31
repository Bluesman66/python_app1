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
            res = input(
                "Did you mean \'{}\' instead? Enter Y if Yes or N if No.".format(match[0]))
            if res == "Y":
                return data[match[0]]
            elif res == "N":
                return "The word \'{}\' does not exist. Please double check it.".format(word)
            else:
                return "Sorry. We didn't understand your entry."
        else:
            return "The word \'{}\' does not exist. Please double check it.".format(word)


word = input("Enter the world: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
