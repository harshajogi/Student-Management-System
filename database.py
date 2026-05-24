import sqlite3

# Connect database
conn = sqlite3.connect("students.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    branch TEXT,
    marks INTEGER
)
""")

# Save changes
conn.commit()

# Close connection
conn.close()

print("Database and table created successfully")
