#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database hbtn_0e_6_usa.

This script connects to a MySQL database specified by command-line arguments,
adds a new State object with the name 'Louisiana' to the 'states' table,
and prints the id of the newly created State.

Args:
    username (str): The username for the MySQL database.
    password (str): The password for the MySQL database.
    database (str): The name of the MySQL database
    containing the 'states' table.

Details:
    - Establishes a connection to the MySQL database on localhost at port 3306.
    - Utilizes SQLAlchemy to add a new State object to the 'states' table.
    - Prints the id of the newly created State.

Example usage:
    $ ./11-model_state_insert.py root root hbtn_0e_6_usa
    6
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    print(louisiana.id)

    session.close()
