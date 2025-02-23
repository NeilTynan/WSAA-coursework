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


# Check to see if the hand contains a Pair, Triple, Straight or Flush

num = [card["value"] for card in hand]
suits = [card["suit"] for card in hand]

test = [1,1,1,4,5]

cnt = Counter()
for value in test:
    cnt[value] += 1
    if cnt[value] == 2 and cnt[value] !=3:
        print("This hand has a Pair")
    elif cnt[value] == 3 and cnt[value] !=2:
        print("This hand has a Triple")

if max(test) - min(test) == 4 and len(test) == 5:
        print("This hand has a Straight.")

if len(set(suits)) == 1:
    print("This hand has a Flush")