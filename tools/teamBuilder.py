from pprint import pprint as pp

def build_optimal_team(characters):
    """
    Fom a dict of characters, extracts the bes combination of 6 characters, 3 for combat and 3 for support following
    this criteria:

    [version beta]
    3 fight are the 3 with most power
    3 support are the next 3 woth most power

    :param characters: dict of characters
    :return: dict: optimal team
    """
    team = {"fight": [], "support": []}
    powers = []

    # Extract the powers and sort them
    for character in characters:
        powers.append(character["_Power"])
    powers.sort()

    # Retrieve the characters with best atributes and save them in a list
    for power in powers[:6]:
        for name in characters.keys():
            if characters[name]["_Power"] == power:
                if len(team["fight"]) < 3:
                    team["fight"].append(name)
                else:
                    team["fight"].append(name)
    pp(team)
    return team

def create_team(chaarcters):
    pass
