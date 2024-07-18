import requests


url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()

print(response['address']['country'])
print(response.get('address').get('country'))



