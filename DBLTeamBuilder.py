from pprint import pprint as pp
from tools.cli import printTitle
from tools.cli import printMenu
from tools.characterManagement import addCharacter

import json

options = {"a": "Add character", "e": "add Equip", "c": "Create team", "p": "Print database", "u": "Update Database"}

if __name__ == '__main__':
    printTitle("Dragon Ball Legends Team Builder")
    option = printMenu(options)
    # characters = loadCharacters()
    pp(characters)
    if option == 'a':
        addCharacter(characters)


