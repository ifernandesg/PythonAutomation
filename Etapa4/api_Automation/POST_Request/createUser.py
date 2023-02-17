import requests
import json

# API URL
# Change createUserFileLocation path
createUserFileLocation = "C:\\Workspace\\Desafios\\Bemol\\Etapa4\\api_Automation\\createUser.json"
createUserUrl = "https://serverest.dev/usuarios"

#Load the json data
file = open(createUserFileLocation, 'r')
jsonInput = file.read()
requestJson = json.loads(jsonInput)

#Create user
createUser = requests.post(createUserUrl, requestJson)
print(createUser.content)

# Verify if user is created
assert createUser.status_code == 201
