# 🖥️ Data Director - Creating an SQLite database with Python

**Course:** Cyber Security Analyst - Technical Foundation Basics | **Date:** 03 July 2025

---

## Task

**Objective:** Create your own SQLite database using Python, define a table, insert data and query it.

---

## Solution

### Python Script (create_database.py)

```python
import sqlite3

# 1. Establish a connection to the database (will be created if it does not exist)
conn = sqlite3.connect("my_creation.db")
cursor = conn.cursor()

# 2. Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS games (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        genre TEXT,
        release_year INTEGER
    )
""")

# 3. Insert data
games_data = [
    ("The Witcher 3", "RPG", 2015),
    ("Minecraft", "Sandbox", 2011),
    ("Portal 2", "Puzzle", 2011),
    ("Elden Ring", "RPG", 2022)
]

cursor.executemany("""
    INSERT INTO games (title, genre, release_year) 
    VALUES (?, ?, ?)
""", games_data)

# Save changes
conn.commit()

# 4. Query and display data
cursor.execute("SELECT * FROM games")
results = cursor.fetchall()

print("All games in the database:")
print("-" * 40)
for row in results:
    print(f"ID: {row[0]}, Title: {row[1]}, Genre: {row[2]}, Year: {row[3]}")

# 5. Close the connection
conn.close()

print("\nDatabase successfully created: my_creation.db")
```

### Output

```
All games in the database:
----------------------------------------
ID: 1, Title: The Witcher 3, Genre: RPG, Year: 2015
ID: 2, Title: Minecraft, Genre: Sandbox, Year: 2011
ID: 3, Title: Portal 2, Genre: Puzzle, Year: 2011
ID: 4, Title: Elden Ring, Genre: RPG, Year: 2022

Database successfully created: my_creation.db
```

---

## Verification

**DB Browser for SQLite:**
1. Open the file `my_creation.db`
2. Select the "Browse Data" tab
3. Click on the "games" table
4. Take a screenshot of the data

---

## Notes

- **`sqlite3.connect()`:** Creates/opens database
- **`cursor.execute()`:** Executes SQL command
- **`cursor.executemany()`:** Executes command for multiple records
- **`?` Placeholder:** Prevents SQL injection
- **`conn.commit()`:** Saves changes
- **`cursor.fetchall()`:** Retrieves all results
- **`CREATE TABLE IF NOT EXISTS`:** Creates only if not already present
- **`INTEGER PRIMARY KEY`:** Auto-increment in SQLite

