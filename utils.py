# Prompts the user with a passed string and lopos if invalid
def getUserInput(inputType="str", prompt=""):
    userInput = input(prompt)

    if (inputType == "str"):
        while (userInput == ""):
            userInput = input(prompt)
    elif (inputType == "int"):
        while (userInput == "" or not userInput.isdigit()):
            userInput = input("Please type an integer: ")

    return userInput