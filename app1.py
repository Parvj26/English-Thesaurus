import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
    

def value(key):
    if key in data:
        value = data[key]
        return (value)
    elif len(get_close_matches(key, data.keys())) > 0:  
        user_input = input("Did you mean %s? Enter Y or N: " %get_close_matches(key, data.keys())[0])
        if user_input == "Y" or user_input == "y" :
            return (data[get_close_matches(key, data.keys())[0]])
        elif user_input == "N" or user_input == "n":
            driver()
        else:
            print("Sorry, What?")
            driver()
    else:
        return ("The word doesn't exist. Please double check")

def driver():
    user_input = input("Enter a Word: ").lower()
    print(value(user_input))

driver()