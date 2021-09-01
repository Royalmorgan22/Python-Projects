""" A simple dictionary code. This program allows the user to search for any word and return the output
 if the word exists in the dictionary. """


# Importing and loading the json file
import json

data = json.load(open('data.json'))


def translate(word):

    if word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("No match found")


# User input

active = True
while active:
    print("Welcome\n")
    word = input("Please enter the word: ")
    result = translate(word)

    print(result)

    again = input("Do you want to search again? y/n: ")
    if again == 'n':
        print("Thank you!")
        active = False
    elif again == 'y':
        continue

