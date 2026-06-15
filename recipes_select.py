import sqlite3

conn = sqlite3.connect('database/recipes.db')
print("Opened database successfully")

cursor = conn.execute("SELECT ID, TITLE, CUISINE, TYPE from RECIPES")
for row in cursor:
    print("ID = ", row[0])
    print("TITLE = ", row[1])
    print("CUISINE = ", row[2])
    print("PREP TIME = ", row[3])

print("Operation done successfully")
conn.close()