import sqlite3

database = 'database/recipes.db'
create_table = [
    '''CREATE TABLE IF NOT EXISTS RECIPES (
        recipe_id INT PRIMARY KEY NOT NULL,
        title CHAR(80) NOT NULL,
        cuisine CHAR(40) NOT NULL,
        tag CHAR(20) NOT NULL,
        prep_time INT NOT NULL,
        cook_time INT NOT NULL,
        servings INT NOT NULL
    );''',

    '''CREATE TABLE IF NOT EXISTS INGREDIENTS (
        ingredient_id INT PRIMARY KEY NOT NULL,
        amount INT NOT NULL,
        ingredient TEXT NOT NULL,
        recipe_id INT NOT NULL,
        FOREIGN KEY (recipe_id) REFERENCES RECIPES (recipe_id)
    );''',

    '''CREATE TABLE IF NOT EXISTS INSTRUCTIONS (
        step_id INT PRIMARY KEY NOT NULL,
        step TEXT NOT NULL,
        recipe_id INT NOT NULL,
        FOREIGN KEY (recipe_id) REFERENCES RECIPES (recipe_id)
    );'''
]

try:
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()

        for statement in create_table:
            cursor.execute(statement)

        conn.commit()

        print("Tables created successfully")
except sqlite3.OperationalError as e:
    print("Failed to create table:", e)
