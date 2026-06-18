import recipes_create as RCreate
import recipes_insert as RInsert
import recipes_select as RSelect
import recipes_update as RUpdate
import recipes_delete as RDelete

from utils import getUserInput

from pathlib import Path

# Declare variables
filePath = Path('database/')
fileName = filePath / 'recipes.db'

# FIRST THINGS FIRST: IF no table exists and user accepts, create RECIPES table (recipes_create); otherwise, exit program
if not (fileName.exists()):
    print("No database exists\nCreating RECIPES database...")
    RCreate.createTable()

# Open menu

# Prompt user input for menu


# MENU OPTION 1 (INSERT): Prompt user input to select which table to insert data into

## Prompt user to insert data
insertData = []
insertData.append(getUserInput("str", "What's your recipe called? "))
insertData.append(getUserInput("str", "What type/nationality of food is it? "))
insertData.append(getUserInput("str", "Give your food a tag (Main dish, Side dish, Dessert, etc.): "))
insertData.append(getUserInput("int", "Prep time? "))
insertData.append(getUserInput("int", "Cook time? "))
insertData.append(getUserInput("int", "How many servings? "))
print(f"{insertData}")
RInsert.insertRecipes(insertData)

## Ask user if he will insert more data and loop if yes; otherwise, exit loop

# MENU OPTION 2: (UPDATE) Prompt user to select the table in which to update existing data

## Prompt user for data to update
##### RUpdate.updateRecipes()

## Ask user if he will update further data and loop if yes; otherwise, exit loop

# MENU OPTION 3 (DELETE): Prompt user to select a table to delete data from

## Prompt user which data should be deleted
##### RDelete.deleteRecipes()

## Ask if user will delete more data and loop if yes; otherwise, exit loop

# MENU OPTION 4 (SELECT/DISPLAY): Prompt user to select between "display all" option or "display one recipe"

## If "display all", display the recipe list in full, with ingredients and instructions
RSelect.displayAll()

## IF "display one recipe", prompt user to select which recipe to display (using Recipe ID)

# IMPORTANT FUNCTIONS
