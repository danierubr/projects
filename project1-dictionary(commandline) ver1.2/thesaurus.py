import json
from difflib import get_close_matches


def search(w):
    w = w.lower().strip()
    if w in data:
        return data[w]
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data:  # in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        answer = input(f"Word not found. Did you mean '{get_close_matches(w, data.keys())[0]}' ? [yes/no] ")
        if answer.strip().lower()[0] == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif answer.strip().lower()[0] == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return f"We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


data = json.load(open('data.json', 'r'))

word = input('Enter a word: ')
output = search(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
