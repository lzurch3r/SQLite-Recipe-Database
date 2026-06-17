import sqlite3

database = 'database/recipes.db'
update_recipes = "UPDATE RECIPES SET\
    title = 'Mangy Oils',\
    cuisine = 'flibbity',\
    tag = 'Harry Potter potions',\
    prep_time = '2000',\
    cook_time = '20',\
    servings = 1\
    WHERE recipe_id = 5"

try:
    with sqlite3.connect(database) as conn:
        cur = conn.cursor()
        cur.execute(update_recipes)
        conn.commit()
except sqlite3.OperationalError as e:
    print(e)