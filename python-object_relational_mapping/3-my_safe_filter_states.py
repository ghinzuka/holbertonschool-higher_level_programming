#!/usr/bin/python3
"""
Write a SAFER script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
Args:
username (str): The username for the MySQL database.
password (str): The password for the MySQL database.
database (str): The name of the MySQL database.
state_name_searched (str): The state name searched.
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    select = """SELECT * FROM states WHERE name = %s ORDER BY id ASC"""
    cursor.execute(select, (state_name_searched,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
