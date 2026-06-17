import sqlite3

database = 'database/recipes.db'
insert_recipes = "INSERT INTO RECIPES ( \
        recipe_id, title, cuisine, tag,\
        prep_time, cook_time, servings\
        )\
    VALUES (\
        3, 'Spaghetti Noodles', 'Italian', 'Main dish',\
        5, 10, 2\
        )"

try:
    with sqlite3.connect(database) as conn:
        cur = conn.cursor()

        conn.execute(insert_recipes)

        conn.commit()

        print("Inserted data successfully")
except sqlite3.OperationalError as e:
    print(e)