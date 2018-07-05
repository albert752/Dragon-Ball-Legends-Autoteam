# EXAMPLE OF A CHARACTER    
# characters = {"Vegeta SP": {"BaseStats":
    # {"HP": 16456}
    # {"SATK": 1460}
    # {"BATK": 2237}
    # {"SDEF": 1243}
    # {"BDEF": 1231}
                                        #, 

                            # "UserStats":
    # {"HP": None}
    # {"SATK": None}
    # {"BATK": None}
    # {"SDEF": None}
    # {"BDEF": None}

    # ,
                            # "SoulBoost":
    # {"HP": None}
    # {"SATK": None}
    # {"BATK": None}
    # {"SDEF": None}
    # {"BDEF": None}

    # ,

    # "Tags": ["Frieza Force", "Saiyan", "Male", "SPARKING", "Ranged", "Purple", "Saiyan", "Saga Z", "Vegeta"],


    # "Level": 1,
    # "Stars": 0
    # }


def loadCharacters ():
    file = open("./database/characters.data", "r")
    characters = json.load(file)
    file.close()
    return characters


def addCharacter(characters = {}, force = False):
    name = input("Enter the name of the character")

    if not force:
        while(name in characters == False):
            name = input("The given name does not correspond to any valid character!\nTry again!")
        character = characters.get(name)
        text = name
    else:
        text = "the new character"

    aux = input("How do you want to set up " + text"?\n[a fo Automatic, m for Manual]... ")

    if aux == "a"
        _addAuto(name)
    if aux == "m"
        _addManual(name)


def _addManual(force):
    pass

def _addAuto():
    pass

if __name__ == "__main__":
    pass
