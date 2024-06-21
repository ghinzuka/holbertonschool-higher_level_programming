#!/usr/bin/python3
"""
Prints the State object with the name passed
as an argument from the database hbtn_0e_6_usa.

This script connects to a MySQL database specified by command-line arguments,
retrieves the State object with the specified name
from the 'states' table in the database,
and prints the State's id. If no state has the
name searched for, it prints "Not found".

Args:
    username (str): The username for the MySQL database.
    password (str): The password for the MySQL database.
    database (str): The name of the MySQL database
    containing the 'states' table.
    state_name (str): The name of the state to search for.

Details:
    - Establishes a connection to the MySQL database on localhost at port 3306.
    - Utilizes SQLAlchemy to query the State object from the 'states' table.
    - The result is the id of the State with the specified name.
    - If no State object is found, prints "Not found".

Example usage:
    $ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
    3
    $ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
    Not found
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
