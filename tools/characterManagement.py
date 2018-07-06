from pprint import pprint as pp
import json

def loadCharacters ():
    file = open("./database/characters.data", "r")
    characters = json.load(file)
    file.close()
    return characters


def addCharacter(characters = {}, force = False):
    '''
    Adds a new characte to the dicst characters. It uses _addAuto and
    _addManual dependin on the user needs. To crate the character first of all
    loads the tempate.Then asks for the name of it and compares thos value to
    the cahracters list. If focer = true means taht we are adding new ones form 
    scratch so it does not check for existance. If not, checks for existance
    and does not proceed until it gets a valid name. Then asks for auto or
    manual set up and calls the apropiated function.
    '''
    # Asks for the name
    name = input("Enter the name of the character: ")

    # Loads the template of the character
    file = open("./templates/character.json", "r")
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
        return _addManual(name, force,  template)


def _addManual(name, force, template):
    '''
    Asks for each parameter in the template and retuns the modified template
    ready to be added to the characters dict

    '''
    pp(template)
    for key in template:
        if ("_" not in key):
            print("\nChanging "+key)
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
