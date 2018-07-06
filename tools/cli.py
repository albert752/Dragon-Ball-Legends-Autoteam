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


def printMenu(options):
    '''
    Prints a menu with the goven options and returns the imput string that the
    user gives.
        Args:
            options: dict of option been the key the letter to press an d the
                     value the string to print with it.
        Returns:
            String: the user's input
    '''
    for key in options.keys():
        print(Fore.CYAN, key + ") " + options[key])
    print(Fore.RESET, end = "")
    printBlanks(2)
    print(Fore.GREEN, "Select your option... ", end="")
    return input()


def printBlanks (number):
    for i in range(number):
        print()


def printCharacter (character):
    printLine()


if __name__ == "__main__":
    printTitle("This is a test title", "YELLOW")
    options = {"a": "Add character", "e": "add Equip", "c": "Create team", "p": "Print database"}
    printBlanks(1)
    printMenu(options)
