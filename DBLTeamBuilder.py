from pprint import pprint as pp
from tools.cli import printTitle
from tools.cli import printMenu
import json

options = {"a": "Add character", "e": "add Equip", "c": "Create team", "p": "Print database", "u": "Update Database"}
characters = {"Gocku": {"Stats": [1, 3]}}

def loadCharacters ():
    global characters
    file = open("./database/characters.data", "r")
    characters = json.load(file)
    file.close()

def addCharacter ():
    continueBool = True
    while(continueBool):
        file = open("./database/characters.data", "w")
        json.dump(characters, file, sort_keys=True, indent=4)
        continueBool = False
        file.close()

if __name__ == '__main__':
    printTitle("Dragon Ball Legends Team Builder")
    option = printMenu(options)
    loadCharacters()
    pp(characters)
    if option == 'a':
        addCharacter()


