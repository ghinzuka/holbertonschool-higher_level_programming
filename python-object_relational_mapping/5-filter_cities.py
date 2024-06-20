#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and lists 
all cities of that state, using the database hbtn_0e_4_usa
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
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    select = """
    SELECT cities.name FROM cities 
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(select, (state_name,))
    cities = cursor.fetchall()
    
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    cursor.close()
    db.close()
