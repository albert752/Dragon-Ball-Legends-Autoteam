from pprint import pprint as pp
from tools.cli import printTitle
from tools.cli import printMenu
from tools.characterManagement import addCharacter
from tools.characterManagement import loadCharacters
from tools.characterManagement import saveCharacters
import json
import os

os.system("clear")

options = {"a": "Add character", "e": "add Equip", "c": "Create team", "p": "Print database", "u": "Update Database", "q": "Quit"}

if __name__ == '__main__':
    characters = loadCharacters()
    exit = False
    while(not exit):
        printTitle("Dragon Ball Legends Team Builder")
        option = printMenu(options)
        if option == 'a':
            addCharacter(characters)
            saveCharacters(characters)
        elif option =='q':
            exit = True
        os.system("clear")
