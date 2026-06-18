import sqlite3

database = 'database/recipes.db'

def insertRecipes(dataArray):
    DATA = dataArray
    print(f"{DATA}")
    try:
        with sqlite3.connect(database) as conn:
            cur = conn.cursor()
            rowsQuery = "SELECT Count() from RECIPES"
            cur.execute(rowsQuery)
            recipe_id = cur.fetchone()[0] + 1

            # insert_recipes = "INSERT INTO RECIPES ( \
            #         recipe_id, title, cuisine, tag,\
            #         prep_time, cook_time, servings\
            #         )\
            #     VALUES (%s, %s, %s, %s, %s, %s, %s)" % (recipe_id,
            #                                             DATA[0],
            #                                             DATA[1],
            #                                             DATA[2],
            #                                             DATA[3],
            #                                             DATA[4],
            #                                             DATA[5])
            conn.execute("INSERT INTO RECIPES (recipe_id, title, cuisine, tag, prep_time, cook_time, servings)\
                VALUES (?, ?, ?, ?, ?, ?, ?)" , (recipe_id,DATA[0],DATA[1],DATA[2],DATA[3],DATA[4],DATA[5]))

            conn.commit()

            print("Inserted data successfully")
    except sqlite3.OperationalError as e:
        print(e)