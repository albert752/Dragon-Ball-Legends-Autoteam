from colorama import Fore, Back, Style, init
from pprint import pprint as pp
import os
import sys
import json


baseCharacters = {}
template = {}

def loadBaseCharacters (reload):
    global baseCharacters
    if os.path.isfile("../databases/baseCharacters.json") == False or reload == True:
        file = open("../databases/baseCharacters.json", "w")
        file.write("{}")
        file.close()
        baseCharacters = {}
    else:
        file = open("../databases/baseCharacters.json", "r")
        baseCharacters = json.load(file)
        file.close()

def addCharacterToBase ():
    global template, baseCharacters
    listOfParams = list(template.keys())
    listOfParams.sort()
    name = input("Enter characters name: ")
    for key in listOfParams:

        # if ("_" in str(key) == True): is not working so I took a diferent aproach
        if(len(key.split("_")) == 2):
            print(Fore.YELLOW, end="")
            print("\nChanging "+key)
            print(Fore.RESET, end="")
            if(type(template[key]) == dict):
                listOfItems = list(template[key].keys())
                listOfItems.sort()
                for item in listOfItems:
                    template[key][item] = int(input("Enter " + item + " value: "))
            elif(type(template[key]) == int):
                template[key] = int(input("Enter " + key + " value: "))
            elif(type(template[key]) == list):
                template[key] = input("Enter the list of tags (, ): ").split(", ")
            elif(template[key] == "Name"):
                template[key] = name
            elif(type(template[key]) == str):
                template[key] = input("Enter " +key+ " value: ")
    # pp(template)
    baseCharacters.update({name: template})
    # pp(baseCharacters)


def reloadTemplate ():
    global template

    link = "../templates/character.json"
    if os.path.isfile(link) == False:
        sys.exit("[ERRO]: Character template not found")
    else:
        file = open(link, "r")
        template = json.load(file)
        file.close()


def saveChanges ():
    global baseCharacters
    file = open("../databases/baseCharacters.json", "w")
    json.dump(baseCharacters, file, sort_keys = True, indent = 4, ensure_ascii = False)
    file.close()


if __name__ == "__main__":
    reload = bool(input("Do you want to reload the file? "))
    loadBaseCharacters(reload)
    cont = True
    while(cont):
        reloadTemplate()
        addCharacterToBase()
        cont = bool(input("Do you want to add another character?"))
    saveChanges()

