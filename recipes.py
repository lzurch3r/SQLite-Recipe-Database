import recipes_create as RCreate
import recipes_insert as RInsert
import recipes_select as RSelect
import recipes_update as RUpdate
import recipes_delete as RDelete

from random import randint

from utils import getUserInput
from utils import isConvertibleToIntStrip
from utils import clearConsole

from pathlib import Path

def main():
    clearConsole()
    # Declare variables
    filePath = Path('database/')
    fileName = filePath / 'recipes.db'
    menu_loop = True

    # FIRST THINGS FIRST: IF no table exists and user accepts, create RECIPES table (recipes_create); otherwise, exit program
    if not (fileName.exists()):
        print("No database exists\nCreating RECIPES database...")
        RCreate.createTable()

    print(f"Opening {fileName}...\n")
    print("Welcome to your recipe list! Here is your menu:")

    while (menu_loop):
        # Open menu
        print("1. Add a recipe")
        print("2. Edit a recipe (under construction)")
        print("3. Delete a recipe")
        print("4. Recipe list display options")
        print("5. Exit program\n")

        # Prompt user input for menu
        menu_option = int(getUserInput("int", "Enter an option: "))

        match menu_option:
            case 1:
                # MENU OPTION 1 (INSERT): Prompt user input to create a new recipe
                ## Prompt user to insert data
                create_recipe_loop = True

                while (create_recipe_loop):
                    RInsert.insertRecipes(createNewRecipe())

                    create_recipe_loop = loopQuery("Add a recipe (Y/N)? ")
                print("Returning to menu...\n")
            
            case 2:
                print("This option is under construction...")
                print("Returning to menu...\n")
                # MENU OPTION 2: (UPDATE) Prompt user to select the table in which to update existing data

                ## Prompt user for data to update
                ##### RUpdate.updateRecipes()

                ## Ask user if he will update further data and loop if yes; otherwise, exit loop

            case 3:
                # MENU OPTION 3 (DELETE): Prompt user to select a table to delete data from

                ## Prompt user which data should be deleted
                delete_loop = True

                while (delete_loop):
                    delete_id = deleteRecipe()
                    if not delete_id == 0:
                        RDelete.deleteRecipes()

                        ## Ask if user will delete more data and loop if yes; otherwise, exit loop
                        delete_loop = loopQuery("Delete another recipe (Y/N)? ")
                    else: delete_loop = False
                print("Returning to menu...\n")

            case 4:
                # MENU OPTION 4 (SELECT/DISPLAY): Prompt user to select between "display all" option or "display one recipe"
                displayOption = getDisplay()

                ## If "All", display the recipe list in full, with ingredients and instructions
                ## Otherwise, display the number selected by the user
                if isConvertibleToIntStrip(displayOption):
                    RSelect.displayOne(displayOption)
                elif displayOption != "EMPTY":
                    RSelect.displayAll()
                print("Returning to menu...\n")
                
            case 5:
                random_exit = randint(1, 3)
                match random_exit:
                    case 1:
                        print("Enjoy your cooking!")
                    case 2:
                        print("¡Buen provecho!")
                    case 3:
                        print("Bon Appétit!")
                    case _:
                        print("See you later!")
                menu_loop = False
            case _:
                print("Invalid input")

# IMPORTANT FUNCTIONS
def createNewRecipe():
    insertData = []
    insertData.append(getUserInput("str", "What's your recipe called? "))
    insertData.append(getUserInput("str", "What type/nationality of food is it? "))
    insertData.append(getUserInput("str", "Give your food a tag (Main dish, Side dish, Dessert, etc.): "))
    insertData.append(getUserInput("int", "Prep time? "))
    insertData.append(getUserInput("int", "Cook time? "))
    insertData.append(getUserInput("int", "How many servings? "))
    #print(f"{insertData}") # DEBUG

    return insertData

def deleteRecipe():
    recipe_count = RSelect.countItems()
    if recipe_count == 0:
        print("No recipes found...")
        return 0
    ask_user_id = int(getUserInput("int", "Pick a recipe to delete (RECIPE ID): "))

    while (ask_user_id <= 0 or ask_user_id > recipe_count):
        ask_user_id = getUserInput("int", f"Please enter a number within range (from 1 to {recipe_count})")
    
    return ask_user_id

def getDisplay():
    recipe_count = RSelect.countItems()
    if recipe_count == 0:
        print("No recipes found...")
        return "EMPTY"
    ask_user = getUserInput("str", "Enter \"All\" to view the whole recipe list or enter a number to view just that recipe: ")
    
    while (True):
        if (isConvertibleToIntStrip(ask_user)):
            if int(ask_user) <= 0 or int(ask_user) > recipe_count:
                ask_user = getUserInput("str", f"Please enter a number within range (from 1 to {recipe_count})")
            else: return ask_user
        elif not isConvertibleToIntStrip(ask_user):
            if ask_user.upper() != "ALL":
                ask_user = getUserInput("str", f"Please enter \"All\" or a number within range (from 1 to {recipe_count})")
            else: return ask_user.upper()

    

def loopQuery(queryString):
    ask_user = getUserInput("str", queryString)
    while (ask_user.upper() != "Y" and ask_user.upper() != "N"):
        ask_user = getUserInput("str", "Please type Y or N and press Enter...")

    if ask_user.upper() == "N":
        return False
    return True

if __name__ == "__main__":
    main()