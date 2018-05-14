import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Y for yes, N for no: " % get_close_matches(word, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Oops, try again then"
        else:
            return "Are you Tottoro? Only Y and N!"
    else:
        return "The word desnt't exist. Please double check it!"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
