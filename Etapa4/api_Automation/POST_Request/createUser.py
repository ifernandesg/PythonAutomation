import requests
import json

#API URL
url = "https://serverest.dev/usuarios"
file = open('C:\\Workspace\\Desafios\\Bemol\\Etapa4\\api_Automation\\createUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)

# Make POST request with Json Input body
postResponse = requests.post(url, request_json)
print(postResponse.content)

assert postResponse.status_code == 201

# Make GET request
getResponse = requests.get(url)
print(getResponse.content)