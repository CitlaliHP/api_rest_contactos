import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"

response = requests.get(URI)

#print(f"GET: {response.text}")
response_json = json.loads(response.text)
for i in range(12):
    print(f"{i+1}.- {response_json['results'][i]['name']}")

opcion = input("Seleccione una opcion: ")
if opcion == "1":
    URI = "https://www.dnd5eapi.co/api/classes/barbarian/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(7):
        print(f"{x+1}.- {response_json['results'][x]['name']}")
elif opcion == "2":
    URI = "https://www.dnd5eapi.co/api/classes/bard/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(8):
        print(f"{x+1}.- {response_json['results'][x]['name']}")

elif opcion == "3":
    URI = "https://www.dnd5eapi.co/api/classes/cleric/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(6):
        print(f"{x+1}.- {response_json['results'][x]['name']}")
elif opcion == "4":
    URI = "https://www.dnd5eapi.co/api/classes/druid/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(16):
        print(f"{x+1}.- {response_json['results'][x]['name']}")

elif opcion == "5":
    URI = "https://www.dnd5eapi.co/api/classes/fighter/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(6):
        print(f"{x+1}.- {response_json['results'][x]['name']}")

elif opcion == "6":
    URI = "https://www.dnd5eapi.co/api/classes/monk/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(4):
        print(f"{x+1}.- {response_json['results'][x]['name']}")

elif opcion == "7":
    URI = "https://www.dnd5eapi.co/api/classes/paladin/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(6):
        print(f"{x+1}.- {response_json['results'][x]['name']}")

elif opcion == "8":
    URI = "https://www.dnd5eapi.co/api/classes/ranger/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(7):
        print(f"{x+1}.- {response_json['results'][x]['name']}")

elif opcion == "9":
    URI = "https://www.dnd5eapi.co/api/classes/rogue/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(9):
        print(f"{x+1}.- {response_json['results'][x]['name']}")

elif opcion == "10":
    URI = "https://www.dnd5eapi.co/api/classes/sorcerer/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(7):
        print(f"{x+1}.- {response_json['results'][x]['name']}")

elif opcion == "11":
    URI = "https://www.dnd5eapi.co/api/classes/warlock/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(4):
        print(f"{x+1}.- {response_json['results'][x]['name']}")

elif opcion == "12":
    URI = "https://www.dnd5eapi.co/api/classes/wizard/proficiencies"
    response = requests.get(URI)
    response_json = json.loads(response.text)
    for x in range(7):
        print(f"{x+1}.- {response_json['results'][x]['name']}")

