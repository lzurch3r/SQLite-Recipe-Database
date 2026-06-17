import sqlite3

database = 'database/recipes.db'


try:
    with sqlite3.connect(database) as conn:
        cur = conn.cursor()
        rowsQuery = "SELECT Count() from RECIPES"
        cur.execute(rowsQuery)
        recipe_id = cur.fetchone()[0] + 1

        
        insert_recipes = "INSERT INTO RECIPES ( \
            recipe_id, title, cuisine, tag,\
            prep_time, cook_time, servings\
            )\
            VALUES (\
            %s, 'Spaghetti Noodles', 'Italian', 'Main dish',\
            5, 10, 2\
            )" % recipe_id
        conn.execute(insert_recipes)

        conn.commit()

        print("Inserted data successfully")
except sqlite3.OperationalError as e:
    print(e)