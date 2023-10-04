import requests

URI = "https://8000-citlalihp-apirestcontac-vvq78fu19gd.ws-us105.gitpod.io/v1/contactos"

response = requests.get(URI)
print(f"GET:{response.text}")
print(f"GET:{response.status_code}")
