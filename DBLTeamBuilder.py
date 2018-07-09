from tools.cli import printTitle
from tools.cli import printMenu
from tools.characterManagement import addCharacter
from tools.characterManagement import loadCharacters
from tools.characterManagement import saveCharacters
from tools.teamBuilder import create_team
import json
import os
import sys

'''
First of all it loads all the characters base information to the baseCharacters
variable form the baseCharacters.json file.
'''
if not os.path.isfile("./tools/databases/baseCharacters.json"):
    sys.exit("[ERROR]: baseCharacters.json file does not exist\n[CLUE]: Reinstall")
else:
    file = open("./tools/databases/baseCharacters.json", "r")
    baseCharacters = json.load(file)
    file.close()

''''
Then it makes sure that a database of user-owned characters exist. If not,
creates an empty one. After that, it creates the variable characters witch
will contain this information.
'''
if os.path.isfile("./database/characters.json"):
    file = open("./database/characters.json", "w")
    file.write("{}")
    file.close()
    characters = {}
else:
    characters = loadCharacters()

os.system("clear")

options = {"a": "Add character", "e": "add Equip", "c": "Create team",
           "p": "Print database", "u": "Update character", "q": "Quit"}

if __name__ == '__main__':
    cont = True
    while cont:
        printTitle("Dragon Ball Legends Team Builder")
        option = printMenu(options)
        if option == 'a':
            addCharacter(characters, baseCharacters)
            saveCharacters(characters)
        elif option == 'c':
            create_team(characters)
        elif option =='q':
            cont = False
        os.system("clear")
