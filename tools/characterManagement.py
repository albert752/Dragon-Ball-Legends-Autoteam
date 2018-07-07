from pprint import pprint as pp
from colorama import Fore, Back, Style, init
import os
import json
import sys

def loadCharacters ():
    file = open("./database/characters.json", "r")
    characters = json.load(file)
    file.close()
    return characters


def saveCharacters (characters):
    file = open("./database/characters.json", "w")
    json.dump(characters, file, sort_keys = True, indent = 4, ensure_ascii = False)
    file.close()


def addCharacter(characters, baseCharacters, force = False):
    ''''
    Creates a character profile form a loaded template. If the parameter force
    equals True, the base stats can be modified, in other cases those are
    locked.

    Args:
        character: dict of characters that is going to be updated.
        force: has a default value of false, enables the edition of base stats
    '''

    # Asks for the name
    print(Fore.YELLOW)
    name = input("Enter the name of the character: ")
    print(Fore.RESET, end="")

    # Checks for force and if false if it's included
    if not force:
        while(not name in list(baseCharacters.keys())):
            name = input("The given name does not correspond to any valid character!\nTry again! ")
        character = characters.get(name)
        text = name
    else:
        text = "the new character"

    aux = input("How do you want to set up " + text + "?\n[a fo Automatic, m for Manual]... ")

    if aux == "a":
        return _addAuto(name, force)
    if aux == "m":
        aux = _addManual(name, force)
        characters.update(aux)
        return aux


def loadTemplate ():
    link = "./tools/templates/character.json"
    if os.path.isfile(link) == False:
        sys.exit("[ERRO]: Character template not found")
    else:
        file = open(link, "r")
        template = json.load(file)
        file.close()
    return template


def _addManual(name, force):
    '''
    Asks for each parameter in the template and retuns the modified template
    ready to be added to the characters dict

    returns:
        dict: dict with character naem as key and character dict as value
    '''
    template = loadTemplate()
    # pp(template)
    listOfParams = list(template.keys())
    listOfParams.sort()
    for key in listOfParams:
        if "_" not in key:
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
            elif(type(template[key]) == str):
                template[key] = input("Enter " +key+ " value: ")
    template["_Power"] = calcPower(template)
    # pp(template)
    return {name: template}


def _addAuto():
    print(Fore.RED, "Sorry, automatically adding characters has not been implemented yet :(")


def calcPower(character):
    '''
    Given a character dict, return  the character z power following the formula
    (hp/15) + SATK + BATK+ SDEF + BDEF + ((crit+ki+valish)/100)*1000

    args:
        character: desired character's dict
    returns:
        int: ZPower
    '''
    baseUsrStats = 0
    for key in character["UserStats"]:
        if key != "HP":
            baseUsrStats = baseUsrStats + character["UserStats"][key]
    hp = character["UserStats"]["HP"]
    otherUserSum = 0
    for key in character["OtherUserStats"]:
        otherUserSum = otherUserSum + character["OtherUserStats"][key]
    Power = (hp/15) + baseUsrStats + ((otherUserSum+2000)/100)*character["Level"]
    return int(Power)


def _starsToPercentage (numStars):
    if numStars == 0:
        return 1
    elif numStars == 1:
        return 1.05
    elif numStars == 2 or numStars == 3:
        return 1.1
    elif numStars == 4 or numStars == 5:
        return 1.15
    elif numStars == 6 or numStars == 7:
        return 1.2
    else:
        return None


# if __name__ == "__main__":
    # print("Welcome to the manual updater")
    # file = open("./databases/baseCharacters.json", "r")
    # characters = json.load(file)
    # pp(characters)
    # file.close()
    # cont = True

    # while(cont):
        # aux = addCharacter(force = True)
        # characters.update(aux)
        # pp(characters)
        # cont = bool(input("continue?  "))
