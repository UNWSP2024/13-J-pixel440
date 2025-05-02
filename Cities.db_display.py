

import sqlite3

def main():
    # connect to the database
    conn = sqlite3.connect('cities.db')
    # connect cursor
    cur = conn.cursor()
    # add the cities table
    add_cities_table(cur)
    # add rows
    add_cities(cur)
    # commit
    conn.commit()
    # display the cities
    display_cities(cur)
    # close connection
    conn.close()


# add the cities table to our database
def add_cities_table(cur):
    # if one already exists, delete it
    cur.execute('DROP TABLE IF EXISTS Cities')
    # create the table
    cur.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY NOT NULL,
                                        CityName TEXT,
                                        Population REAL)''')
# provide city data to populate the table
def add_cities(cur):
    cities_pop = [(1, 'Tokyo', 38001000),
                  (2, 'Delhi', 25703168),
                  (3, 'Shanghai', 23740778),
                  (4, 'Sao Paulo', 21066245),
                  (5, 'Mumbai', 21042538),
                  (6, 'Mexico City', 20998543),
                  (7, 'Beijing', 20383994),
                  (8, 'Osaka', 20237645),
                  (9, 'Cairo', 18771769),
                  (10, 'New York', 18593220),
                  (11, 'Dhaka', 17598228),
                  (12, 'Karachi', 16617644),
                  (13, 'Buenos Aires', 15180176),
                  (14, 'Kolkata', 14864919),
                  (15, 'Istanbul', 14163989),
                  (16, 'Chongqing', 13331579),
                  (17, 'Lagos', 13122829),
                  (18, 'Manila', 12946263),
                  (19, 'Rio de Janeiro', 12902306),
                  (20, 'Guangzhou', 12458130)]

    for row in cities_pop:
        cur.execute('''INSERT INTO Cities (CityID, CityName, Population)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

# to display the cities table
def display_cities(cur):
    print('Contents of cities.db/Cities table:')
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

# instance to run the main function
if __name__ == '__main__':
    main()
