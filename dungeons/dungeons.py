import requests
import json


URI = "https://www.dnd5eapi.co/api/classes"

response = requests.get(URI)

#print(f"GET: {response.text}")

response_json = json.loads(response.text)

print(f"{response_json['results'][0]['name']}")
