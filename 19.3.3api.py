import requests  # библиотека запросов
import json

base_url = "https://petstore.swagger.io/v2/"

# Find Pets by status GET запрос
res = requests.get(base_url + 'pet/findByStatus', params={'status': 'available'},
                           headers={'accept': 'application/json'})
status = res.status_code
result = ""
try:
    result = res.json()
except:
    result = res.text
print('Find Pets by status GET запрос')
print(f'Статус код: {status}')
print(result)
print('-----')


# Add a new pet to the store POST запрос
headers = {'accept': 'application/json'}
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Jora",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res = requests.post(base_url + 'pet', headers=headers, json=data)
status = res.status_code
result = ""
try:
    result = res.json()
except:
    result = res.text
print('Add a new pet to the store POST запрос')
print(f'Статус код: {status}')
print(result)
print('-----')


# Delete a pet DELETE запрос
headers = {'accept': 'application/json', 'api_key': 'api_key'}
petId = 'id'  # указывается id удаляемого объекта
res = requests.delete(base_url + 'pet/' + petId, headers=headers)
status = res.status_code
result = ""
try:
    result = res.json()
except:
    result = res.text
print('Delete a pet DELETE запрос')
print(f'Статус код: {status}')
print(result)
print('-----')


# Update an existing pet PUT запрос
headers = {'accept': 'application/json'}
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Urchik",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res = requests.put(base_url + 'pet', json=data)
status = res.status_code
result = ""
try:
    result = res.json()
except:
    result = res.text
print('Update an existing pet PUT запрос')
print(f'Статус код: {status}')
print(result)