import requests
endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, json={"data": "assigned in the body"}, params={"author":"Zenebe Wela"})
print(response.json())
