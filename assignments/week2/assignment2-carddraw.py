#Import Libraries

import requests
import json
from collections import Counter


# Shuffle the deck

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
shuffle = response.json()
deck = shuffle["deck_id"]


# Draw Cards from the Deck

url2 = "https://deckofcardsapi.com/api/deck/{deck}/draw/?count=5".format(deck=deck)
fivecards = requests.get(url2)


# Display Five Cards Drawn

deal = fivecards.json()
hand = deal["cards"]

def draw():
    for card in hand:
        print(card["value"],"of",card["suit"])


# Check to see if the hand contains a Pair, Triple, Straight or Flush, making sure only to list the highest hand

face = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'JACK': 11, 'QUEEN': 12, 'KING': 13, 'ACE': 14} # Converting face cards to integers as part of straight analysis
num = Counter(card["value"] for card in hand)
suits = [card["suit"] for card in hand]

cnt = num

def result():
    for value, count in cnt.items():
        if len(set(suits)) == 1:
            print("Congratualation!This hand has a Flush")
            break
        if len(set(face[card["value"]] for card in hand)) == 5 and max(face[card["value"]] for card in hand) - min(face[card["value"]] for card in hand) == 4: # Converting card values into those in face or else the mix of string and integers causes issues
            print("Congratualation! This hand has a Straight.")
            break

        if count == 3:
            print("Congratualation! This hand has a Triple")
            break
        elif count == 2:
            print("Congratualation! This hand has a Pair") 
            break 

# Draw a hand and get the result if it is a pair, triple, flush or stright
draw()
result()
