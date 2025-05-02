

import sqlite3

# define a name for the database
db_name = "phonebook.db"

# create and define the phonebook class
class Phonebook:
    def __init__(self, db_name):
        self.db_name = db_name
        self.create_database()



    # make sure database and table is created
    def create_database(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS Entries (
                    name TEXT PRIMARY KEY,
                    phone TEXT NOT NULL
                )
            ''')



    # user data entry function
    def add_entry(self, name, phone):
        try:
            with sqlite3.connect(self.db_name) as conn:
                conn.execute("INSERT INTO Entries (name, phone) VALUES (?, ?)", (name, phone))
                print(f"{name}'s entry added.")
        except sqlite3.IntegrityError:
            print("Name already exists in the phonebook.")

    # phone number lookup function
    def lookup_entry(self, name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute("SELECT phone FROM Entries WHERE name = ?", (name,))
            result = cursor.fetchone()
        if result:
            print(f"{name}'s number is: {result[0]}")
        else:
            print("Name not found in phonebook.")

    # phone number update function
    def update_entry(self, name, new_phone):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute("UPDATE Entries SET phone = ? WHERE name = ?", (new_phone, name))
            if cursor.rowcount:
                print(f"Updated {name}'s phone number.")
            else:
                print("Name not found in phonebook.")

    # delete number by name funciton
    def delete_entry(self, name):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute("DELETE FROM Entries WHERE name = ?", (name,))
            if cursor.rowcount:
                print(f"Deleted {name}'s information.")
            else:
                print("Name not found.")


# user interface and main menu
def main():
    pb = Phonebook(db_name)

    # menu options
    options = {
        '1': ("Add entry", pb.add_entry),
        '2': ("Look up entry", pb.lookup_entry),
        '3': ("Update entry", pb.update_entry),
        '4': ("Delete entry", pb.delete_entry),
        '5': ("Exit", None)
    }

    # menu system loop
    while True:
        print("\nPhonebook Menu:")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        choice = input("Choose an option (1-5): ").strip()

        # input handling
        if choice == '1':
            pb.add_entry(input("Enter name: ").strip(), input("Enter phone number: ").strip())
        elif choice == '2':
            pb.lookup_entry(input("Enter name to look up: ").strip())
        elif choice == '3':
            pb.update_entry(input("Enter name to update: ").strip(), input("Enter new phone number: ").strip())
        elif choice == '4':
            pb.delete_entry(input("Enter name to delete: ").strip())
        elif choice == '5':
            print("Exit successful")
            break
        else:
            print("Invalid option. Please try again.")

# run the program
if __name__ == "__main__":
    main()
