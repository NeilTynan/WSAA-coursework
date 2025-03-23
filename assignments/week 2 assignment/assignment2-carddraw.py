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
for card in hand:
    print(card["value"],"of",card["suit"])


# Check to see if the hand contains a Pair, Triple, Straight or Flush, making sure only to list the highest hand

num = [card["value"] for card in hand]
suits = [card["suit"] for card in hand]

cnt = Counter(num)

for value, count in cnt.items():
    if count == 2:
        print("This hand has a Pair") 
        break 
    elif count == 3:
        print("This hand has a Triple")
        break
    elif len(set(num)) == 5 and max(num) - min(num) == 4: 
        print("This hand has a Straight.")
        break
    elif len(set(suits)) == 1:
        print("This hand has a Flush")
        break