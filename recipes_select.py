import sqlite3

database = 'database/recipes.db'
select_recipes = "SELECT * from RECIPES"
select_ingredients = "SELECT * from INGREDIENTS"

def countItems():
    try:
        with sqlite3.connect(database) as conn:
            cur = conn.cursor()

            cur.execute("SELECT Count() from RECIPES")

            item_count = cur.fetchone()[0]
            
            return item_count
    except sqlite3.OperationalError as e:
        print(e)
    return 0

def displayOne(recipe_id):
    try:
        with sqlite3.connect(database) as conn:
            cur_recipes = conn.cursor()
            cur_ingredients = conn.cursor()
            cur_instructions = conn.cursor()

            cur_recipes.execute("SELECT * FROM RECIPES WHERE recipe_id=?", (recipe_id,))

            recipe_info = cur_recipes.fetchone()
            print("Recipe ID:", recipe_info[0])
            print("Title:", recipe_info[1])
            print("Cuisine/Genre:", recipe_info[2])
            print("Tag:", recipe_info[3])
            print("Prep time:", recipe_info[4], "minutes")
            print("Cook time:", recipe_info[5], "minutes")
            print("Servings:", recipe_info[6])
    except sqlite3.OperationalError as e:
        print(e)

def displayAll():
    try:
        with sqlite3.connect(database) as conn:
            cursor_recipes = conn.cursor()
            cursor_ingredients = conn.cursor()
            cursor_instructions = conn.cursor()

            cursor_recipes.execute(select_recipes)

            rows = cursor_recipes.fetchall()

            # Display all of the recipes in the list
            for row in rows:
                print("Recipe ID:", row[0])
                print("Title:", row[1])
                print("Cuisine/Genre:", row[2])
                print("Tag:", row[3])
                print("Prep time:", row[4], "minutes")
                print("Cook time:", row[5], "minutes")
                print("Servings:", row[6])

                # Move on to displaying the ingredients for each recipe
                recipe_id = row[0]
                count_query = cursor_ingredients.execute("SELECT Count() from INGREDIENTS WHERE recipe_id=?", (recipe_id,))
                row_count = count_query.fetchone()[0]
                # If there are no steps, skip the process of querying more data
                # Otherwise, query the instruction steps and display them all
                if (row_count > 0):
                    print("   Ingredients:")
                    ing_rows = cursor_ingredients.execute("SELECT * from INGREDIENTS WHERE recipe_id=?", (recipe_id,))
                    for ing_row in ing_rows:
                        print(f"      - {ing_row[1]} {ing_row[2]}")
                
                # Move on to displaying the steps for each recipe
                count_query = cursor_instructions.execute("SELECT Count() from INSTRUCTIONS WHERE recipe_id=?", (recipe_id,))
                row_count = count_query.fetchone()[0]
                # If there are no steps, skip the process of querying more data
                # Otherwise, query the instruction steps and display them all
                if (row_count > 0):
                    print("   Instructions:")
                    ins_rows = cursor_instructions.execute("SELECT * from INSTRUCTIONS WHERE recipe_id=?", (recipe_id,))
                    for ins_row in ins_rows:
                        print("      Step", ins_row[0])
                        print("        ", ins_row[1])
                print("")

    except sqlite3.OperationalError as e:
        print(e)

if __name__ == "__main__":
    displayAll()