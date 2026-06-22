import os
# Prompts the user with a passed string and lopos if invalid
def getUserInput(inputType="str", prompt=""):
    userInput = input(prompt)

    if (inputType == "str"):
        while (userInput == ""):
            userInput = input(f"Please try typing something else\n{prompt}")
    elif (inputType == "int"):
        while (userInput == "" or not userInput.isdigit()):
            userInput = input("Please type an integer: ")

    return userInput

def isConvertibleToIntStrip(s):
    s = s.strip()
    try:
        int(s)
        return True
    except ValueError:
        return False

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')