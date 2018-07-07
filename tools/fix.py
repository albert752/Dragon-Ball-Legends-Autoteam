import json
from pprint import pprint as pp
# EXAMPLE OF A CHARACTER    
character = {"_BaseStats": {"HP": -1, "SATK": -1, "BATK": -1, "SDEF": -1, "BDEF": -1}, "UserStats": {"HP": -1, "SATK": -1, "BATK": -1, "SDEF": -1, "BDEF": -1}, "SoulBoost": {"HP": -1, "SATK": -1, "BATK": -1, "SDEF": -1, "BDEF": -1}, "_Tags": [], "Level": -1, "Stars": -1, "_OtherBaseStats": {"Crit": -1, "Ki": -1}, "OtherUserStats": {"Crit": -1, "Ki": -1}, "OtherSoulBoost": {"Crit": -1, "Ki": -1}, "EquipmentSlots": -1, "_Power": -1}


pp(character)
file = open("./templates/character.json", "w")
json.dump(character, file, sort_keys = True, indent = 4, ensure_ascii = False)
file.close()

file = open("./templates/character.json", "r")
pp(json.load(file))
file.close()
