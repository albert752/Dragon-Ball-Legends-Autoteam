import json
from pprint import pprint as pp
# EXAMPLE OF A CHARACTER    
character = {"BaseStats": {"HP": 16456, "SATK": 1460, "BATK": 2237, "SDEF": 1243, "BDEF": 1231}, "UserStats": {"HP": 268571, "SATK": 24245, "BATK": 34393, "SDEF": 19765, "BDEF": 19523}, "SoulBoost": {"HP": 30065, "SATK": 3038, "BATK": 2155, "SDEF": 1792, "BDEF": 1732}, "Tags": ["Frieza Force", "Saiyan", "Male", "SPARKING", "Ranged", "Purple", "Saiyan", "Saga Z", "Vegeta"], "Level": 1000, "Stars": 3, "OtherBaseStats": {"Crit": 0, "Ki": 0}, "OtherUserStats": {"Crit": 1068, "Ki": 1874}, "OtherSoulBoost": {"Crit": 67, "Ki": 0}, "EquipmentSlots": 1, "ZPower": 0}


pp(character)
file = open("./templates/character.json", "w")
json.dump(character, file, sort_keys = True, indent = 4, ensure_ascii = False)
file.close()

file = open("./templates/character.json", "r")
pp(json.load(file))
file.close()
