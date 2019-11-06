import requests
import json

apiKey ='37134fea34fc11b5bdc5e82ad894109b3d141674'
url = 'http://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()
#print(responst.json)

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)
