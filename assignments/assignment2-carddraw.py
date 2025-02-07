import requests
import json

# Shuffle the deck
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
shuffle = response.json()
deck = shuffle["deck_id"]
deck

# Draw Cards
url2 = "https://deckofcardsapi.com/api/deck/{deck}/draw/?count=5".format(deck=deck)
new_deck = requests.get(url2)
deal = new_deck.json()
cards = deal["cards"]
for i in cards:
    print(i["value"],"of",i["suit"])
