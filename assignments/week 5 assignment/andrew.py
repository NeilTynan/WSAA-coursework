import requests
from config import config as cfg
import json

url = 'https://api.github.com/repos/NeilTynan/aprivateone/contents/andrew.py'
apikey = cfg("gkey")

# Check the url and apikey are working
response = requests.get(url, auth = ('token', apikey))
print(response.status_code)

# Convert the response data into json
data = response.json()

# If statment that triggers if the response is successful
if response.status_code == 200:

    # Update the response data with the new value
    content = data['content']
    update = content.replace('Andrew', 'Neil')

    # Commit message that is sent with the data update
    commit = {
        'message': 'Replaced Andrew with Neil',
        'content': new_content,
        'sha': data['sha'],
        'branch': 'main'
    }

    # Put request to send back the updated data and the commitment message
    response2 = requests.put(url, json=commit, headers={'Authorization': f'token {apikey}'})
    print(response2.status_code)
else:
    print('Error') 