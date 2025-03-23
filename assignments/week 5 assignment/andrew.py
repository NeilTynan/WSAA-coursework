import requests
from config import config as cfg
import json

filename="andrew.txt"
url = 'https://api.github.com/repos/NeilTynan/aprivateone'
apikey = cfg("gkey")

response = requests.get(url, auth = ('token', apikey))

print (response.status_code)

with open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)