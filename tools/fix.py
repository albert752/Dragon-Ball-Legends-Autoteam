import json
from pprint import pprint as pp
# EXAMPLE OF A CHARACTER    
character = {"Name":"Vegeta SP", "BaseStats": {"HP": 16456, "SATK": 1460, "BATK": 2237, "SDEF": 1243, "BDEF": 1231}, "UserStats": {"HP": None, "SATK": None, "BATK": None, "SDEF": None, "BDEF": None}, "SoulBoost": {"HP": None, "SATK": None, "BATK": None, "SDEF": None, "BDEF": None}, "Tags": ["Frieza Force", "Saiyan", "Male", "SPARKING", "Ranged", "Purple", "Saiyan", "Saga Z", "Vegeta"], "Level": 1, "Stars": 0}


pp(character)
file = open("./templates/character.json", "w")
json.dump(character, file, sort_keys = True, indent = 4, ensure_ascii = False)
file.close()

file = open("./templates/character.json", "r")
pp(json.load(file))
file.close()
