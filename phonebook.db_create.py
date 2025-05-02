

import sqlite3

# create database
conn = sqlite3.connect('phonebook.db')

# import cursor
cursor = conn.cursor()

# create the entries table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL
    )
''')

# commit
conn.commit()
# close
conn.close()
