#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

This script connects to a MySQL database specified by command-line arguments,
queries the first State object from the 'states' table in the database,
and prints the State's id and name.

Args:
    username (str): The username for the MySQL database.
    password (str): The password for the MySQL database.
    database (str): The name of the MySQL database
    containing the 'states' table.

Details:
    - Establishes a connection to the MySQL database on localhost at port 3306.
    - Utilizes SQLAlchemy to query the first State object from the 'states'
    - Prints the first State object in the format "{id}: {name}".
    - If the 'states' table is empty, prints "Nothing".

Example usage:
    $ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
    1: California
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

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
