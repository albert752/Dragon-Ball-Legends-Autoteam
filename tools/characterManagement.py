from pprint import pprint as pp
import json
from colorama import Fore, Back, Style, init

def loadCharacters ():
    file = open("./database/characters.json", "r")
    characters = json.load(file)
    file.close()
    return characters


def saveCharacters (characters):
    file = open("./database/characters.json", "w")
    json.dump(characters, file, sort_keys = True, indent = 4, ensure_ascii = False)
    file.close()


def addCharacter(characters = {}, force = False):
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
    # Loads the template of the character
    # (Path relative to main file)
    file = open("./tools/templates/character.json", "r")
    template = json.load(file)
    file.close()

    # Checks for force and if false if it's included
    if not force:
        while(name in characters == False):
            name = input("The given name does not correspond to any valid character!\nTry again! ")
        character = characters.get(name)
        text = name
    else:
        text = "the new character"

    aux = input("How do you want to set up " + text + "?\n[a fo Automatic, m for Manual]... ")

    if aux == "a":
        return _addAuto(name, force, template)
    if aux == "m":
        aux = _addManual(name, force,  template)
        characters.update(aux)
        return aux


def _addManual(name, force, template):
    '''
    Asks for each parameter in the template and retuns the modified template
    ready to be added to the characters dict
    '''

    pp(template)
    for key in template:
        if ("_" not in key):
            print(Fore.YELLOW, end="")
            print("\nChanging "+key)
            print(Fore.RESET, end="")
            if(type(template[key]) == dict):
                for item in template[key]:
                    template[key][item] = int(input("Enter " + item + " value: "))
            elif(type(template[key]) == int):
                template[key] = int(input("Enter " + key + " value: "))
            elif(type(template[key]) == list):
                template[key] = input("Enter the list of tags (, ): ").split(", ")
            elif(template[key] == "Name"):
                template[key] = name
            elif(type(template[key]) == str):
                template[key] = input("Enter " +key+ " value: ")
    pp(template)
    return {name: template}



def _addAuto():
    pass


if __name__ == "__main__":
    print("Welcome to the manual updater")
    file = open("./databases/baseCharacters.json", "r")
    characters = json.load(file)
    pp(characters)
    file.close()
    cont = True

    while(cont):
        aux = addCharacter(force = True)
        characters.update(aux)
        pp(characters)
        cont = bool(input("Continue?  "))

    file = open("./databases/baseCharacters.json", "w")
    json.dump(characters, file, sort_keys = True, indent = 4, ensure_ascii = False)
    file.close()
