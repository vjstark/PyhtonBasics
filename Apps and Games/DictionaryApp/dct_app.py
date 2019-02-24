import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()

    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Y/N." %get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist"
        else:
            return "We did not understand your input"
    else:
        return "The word was not found."



word = input("Enter the word: ")
output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
