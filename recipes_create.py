import sqlite3

conn = sqlite3.connect('database/recipes.db')
print("Opened database successfully")

conn.execute(
    '''CREATE TABLE IF NOT EXISTS RECIPES
    (
        ID INT PRIMARY KEY NOT NULL,
        TITLE TEXT NOT NULL,
        CUISINE TEXT NOT NULL,
        TYPE TEXT NOT NULL
    );''')
print("Table created successfully")

conn.close()