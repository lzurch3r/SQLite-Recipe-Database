import sqlite3

database = 'database/recipes.db'
select_recipes = "SELECT * from RECIPES"
select_ingredients = "SELECT * from INGREDIENTS"
select_instructions = "SELECT * from INSTRUCTIONS"

try:
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()

        cursor.execute(select_recipes)

        rows = cursor.fetchall()

        for row in rows:
            print("Recipe ID:", row[0])
            print("Title:", row[1])
            print("Cuisine/Genre:", row[2])
            print("Tag:", row[3])
            print("Prep time:", row[4], "minutes")
            print("Cook time:", row[5], "minutes")
            print("Servings:", row[6])
            print("")

        cursor.execute(select_instructions)

        rows = cursor.fetchall()

        for row in rows:
            print("Recipe ID:", row[2])
            print("Step:", row[0])
            print(row[1])

except sqlite3.OperationalError as e:
    print(e)

