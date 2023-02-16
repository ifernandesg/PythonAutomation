import requests
import json
import jsonpath

# API URL
urlLogin = "https://serverest.dev/login"
fileLogin = open('C:\\Workspace\\Desafios\\Bemol\\Etapa4\\api_Automation\\loginCredentials.json', 'r')
jsonLogin_input = fileLogin.read()
requestLoginBody = json.loads(jsonLogin_input)

productUrl = "https://serverest.dev/produtos"
file = open('C:\\Workspace\\Desafios\\Bemol\\Etapa4\\api_Automation\\createProduct.json', 'r')
json_input = file.read()
requestProductBody = json.loads(json_input)

# POST request to login
postResponseLogin = requests.post(urlLogin, requestLoginBody)
print(postResponseLogin.content)

# Get authorization value

responseLogin = json.loads(postResponseLogin.text)
authorizationLoginToken = jsonpath.jsonpath(responseLogin, 'authorization')
print(authorizationLoginToken[0])

headers = {'Authorization': authorizationLoginToken[0]}

# authorize = requests.get('https://serverest.dev/', headers=headers)
# print(authorize.json)

# POST request to create product
productResponse = requests.post(productUrl, requestProductBody, headers=headers)
print(productResponse.content)

assert productResponse.status_code == 201