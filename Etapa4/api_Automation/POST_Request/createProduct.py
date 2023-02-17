import requests
import json
import jsonpath

# Login URL
# Change loginCredentialsFileLocation path
urlLogin = "https://serverest.dev/login"
loginCredentialsFileLocation = open('C:\\Workspace\\Desafios\\Bemol\\Etapa4\\api_Automation\\loginCredentials.json', 'r')
jsonLogin_input = loginCredentialsFileLocation.read()
requestLoginBody = json.loads(jsonLogin_input)

# Product URL 
# Change createProductFileLocation path
productUrl = "https://serverest.dev/produtos"
createProductFileLocation = open('C:\\Workspace\\Desafios\\Bemol\\Etapa4\\api_Automation\\createProduct.json', 'r')
json_input = createProductFileLocation.read()
requestProductBody = json.loads(json_input)

# POST request to login
postResponseLogin = requests.post(urlLogin, requestLoginBody)
print(postResponseLogin.content)

# Get authorization value
responseLogin = json.loads(postResponseLogin.text)
authorizationLoginToken = jsonpath.jsonpath(responseLogin, 'authorization')
print(authorizationLoginToken[0])
headers = {'Authorization': authorizationLoginToken[0]}

# Create product
productResponse = requests.post(productUrl, requestProductBody, headers=headers)
print(productResponse.content)

# Verify if product is created
assert productResponse.status_code == 201