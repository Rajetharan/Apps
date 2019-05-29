import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()

    if w in data:
        return data[w]

    elif w.title() in data: #if user entered "texas", this will convert to "Texas"
        return data[w.title()]

    elif w.upper() in data: #for words like USA or NATO
        return data[w.upper()]

    elif len(get_close_matches(w,data.keys())) > 0:
        close_match = get_close_matches(w,data.keys(),n=1,cutoff=0.8)[0]
        answer = input("Did you mean %s instead? Enter Y for yes or N for no: " % close_match)

        if answer == "Y":
            return data[close_match]

        elif answer == "N":
            return("Word does not exist.")

        else:
            return ("We didn't understand your entry.")

    else:
        return("Word does not exist.")

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
