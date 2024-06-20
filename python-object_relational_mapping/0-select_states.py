#!/usr/bin/python3
import sys
import MySQLdb
"""
Connects to a MySQL database and selects all states from the 'states' table.

Args:
	username (str): The username for the MySQL database.
	password (str): The password for the MySQL database.
	database (str): The name of the MySQL database.
	"""

if __name__ == "__main__":
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
