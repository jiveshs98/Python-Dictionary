import json
from difflib import get_close_matches

data= json.load(open("data.json"))

def dictionary(key):

    key= key.lower()

    if key in data:         # If word is present in dictionary
        return data[key]

    elif key.upper() in data:   # If there is any acronym like USA, NATO, UN, IPC etc
        return data[key.upper()]

    elif key.title() in data:   # If there is a word starting with a capital letter such as nouns: Delhi
        return data[key.title()]

    elif len(get_close_matches(key,data.keys()))>0:     # If there is any possibility of a similar word
        match= get_close_matches(key,data.keys())[0]
        ch= input("\nDid you mean %s? Enter 'y' for yes and 'n' for no : " % match)
        ch= ch.upper()

        if ch == 'Y':
            return data[match]

        elif ch == 'N':
            return "Sorry! This word doesn't exist. Please double check it.\n"

        else:
            return "Invalid response!!!\n"

    else:
        return "Sorry! This word doesn't exist. Please double check it.\n"


word= input("\nEnter a word: ")
meaning= dictionary(word)
print("\n")

if type(meaning) == list:
    for i in meaning:
        print("--> %s\n"%i)
else:
    print(meaning)
