#!/usr/bin/python3
"""
Connects to a MySQL database and selects all
states with a name starting with 'N'
from the 'states' table.
Args:
username (str): The username for the MySQL database.
password (str): The password for the MySQL database.
database (str): The name of the MySQL database.
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    select = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(select)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
