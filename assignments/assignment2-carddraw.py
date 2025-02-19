import requests
import json

# Shuffle the deck
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
shuffle = response.json()
deck = shuffle["deck_id"]

# Draw Cards
url2 = "https://deckofcardsapi.com/api/deck/{deck}/draw/?count=5".format(deck=deck)
fivecards = requests.get(url2)
deal = fivecards.json()
hand = deal["cards"]
for card in hand:
    print(card["value"],"of",card["suit"])