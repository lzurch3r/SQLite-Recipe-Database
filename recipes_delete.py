import sqlite3

def deleteRecipes(id):
    database = 'database/recipes.db'
    if id != 0:
        try:
            with sqlite3.connect(database) as conn:
                cur = conn.cursor()
                cur_update = conn.cursor()
                cur.execute("DELETE from RECIPES WHERE recipe_id = ?", (id,))

                # Update all the recipe_id's for the items in the table
                cur_update.execute("SELECT recipe_id FROM RECIPES ORDER BY recipe_id")
                rows = cur_update.fetchall()

                row_count = 1        
                for row in rows:
                    #print(f"Recipe ID: {row[0]}, row count: {row_count}") # DEBUG
                    if (row[0] != row_count):
                        update_recipes = "UPDATE RECIPES SET recipe_id = ? WHERE recipe_id = ?"
                        cur_update.execute(update_recipes, (row_count,row[0]))
                    row_count += 1
                    #print("Recipe IDs updated successfully") # DEBUG
                print(f"Recipe deleted successfully!")
                conn.commit()
        except sqlite3.OperationalError as e:
            print(e)

if __name__ == "__main__":
    deleteRecipes(0)