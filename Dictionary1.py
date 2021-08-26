""" A simple dictionary code. This program allows the user to search any word and return the output
 if the word exists in the dictionary. """

# Importing the json module

import json

# loading and opening the json dictionary file.

data = json.load(open('data.json'))


# Defining the word translation

def translate(word):
    # The program returns the word even if its entered either in upper or lower case as well as with title
    if word.lower() in data:
        return data[word.lower()]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("No match found")

# User input and returning the result.
word = input("Please enter the word: ")
result = translate(word)

print(result)
