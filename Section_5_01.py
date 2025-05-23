import sqlite3

# 1. Connect to database (file create hoga agar nahi hai)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 2. Drop table if exists (clean start for testing)
cursor.execute("DROP TABLE IF EXISTS users")
conn.commit()

# 3. Create table with UNIQUE constraint on 'name'
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    age INTEGER
)
''')
conn.commit()

# 4. Function to insert user only if name not exists
def insert_user(name, age):
    cursor.execute("SELECT * FROM users WHERE name=?", (name,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        print(f"Inserted {name}")
    else:
        print(f"{name} already exists, skipping insert")

# 5. Function to read all users
def read_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("\nAll users in DB:")
    for row in rows:
        print(row)

# 6. Function to update user age by name
def update_user_age(name, new_age):
    cursor.execute("UPDATE users SET age=? WHERE name=?", (new_age, name))
    conn.commit()
    print(f"Updated {name}'s age to {new_age}")

# 7. Function to delete user by name
def delete_user(name):
    cursor.execute("DELETE FROM users WHERE name=?", (name,))
    conn.commit()
    print(f"Deleted user {name}")

# --- Testing all functions ---

insert_user("Alice", 30)
insert_user("Bob", 25)
insert_user("Alice", 40)  # Duplicate, will skip

read_users()

update_user_age("Bob", 26)
read_users()

delete_user("Alice")
read_users()

# 8. Close connection at end
conn.close()
