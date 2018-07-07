from colorama import Fore, Back, Style, init

init()

def printLine(length, line = "-", notch = "%"):
    print(Fore.YELLOW, "%", end = '')
    for i in range(length+2):
        print("-", end = "")
    print("%", end="")
    print(Fore.RESET)


def printTitle (text, colour="YELLOW", line = "-", notch = "%"):
    printLine(len(text))
    print(Fore.YELLOW, "| " + text + " |")
    printLine(len(text))


def printMenu(optionsDicts):
    """
    Prints a menu with the given options and returns the imput string that the
    user gives.
        Args:
            optionsDicts: dict of option been the key the letter to press an d the
                     value the string to print with it.
        Returns:
            String: the user's input
    """
    optionsList = list(optionsDicts.keys())
    optionsList.sort()
    for key in optionsList:
        print(Fore.CYAN, key + ") " + optionsDicts[key])
    print(Fore.RESET, end = "")
    printBlanks(2)
    print(Fore.GREEN, "Select your option... ", end="")
    return input()


def printBlanks (number):
    """
    Prints a number of blank spaces given by parameter
    :param number: number of white spaces
    :return: None
    """
    for i in range(number):
        print()


if __name__ == "__main__":
    printTitle("This is a test title", "YELLOW")
    options = {"a": "Add character", "e": "add Equip", "c": "Create team", "p": "Print database"}
    printBlanks(1)
    printMenu(options)
