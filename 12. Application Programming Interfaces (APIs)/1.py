import requests

request = "https://api.chucknorris.io/jokes/random"

response = requests.get(request).json()
print(response['value'])