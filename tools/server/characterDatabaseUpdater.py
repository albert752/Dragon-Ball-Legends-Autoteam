from colorama import Fore, Back, Style, init
from pprint import pprint as pp
import os
import sys
import json


baseCharacters = {}
template = {}

def openBaseCharacters ():
    global baseCharacters
    if os.path.isfile("../databases/baseCharacters.json") == False:
        open("../databases/baseCharacters.json", "w").close()
        baseCharacters = {}
    else:
        file = open("../databases/baseCharacters.json", "r")
        baseCharacters = json.load(file)
        file.close()

def addCharacterToBase ():
    global template, baseCharacters
    listOfParams = list(template.keys())
    listOfParams.sort()
    template["Name"] = input("Enter characters name: ")
    for key in listOfParams:
        pp(key)
        if ("_" in str(key) == True):
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
    baseCharacters.update({template["Name"]: template})
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
    openBaseCharacters()
    cont = True
    while(cont):
        reloadTemplate()
        addCharacterToBase()
        cont = bool(input("Do you want to add another character?"))
    saveChanges()

