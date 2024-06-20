#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.

This script connects to a MySQL database specified by command-line arguments,
retrieves all State objects from the 'states' table in the database, and prints
each State's id and name in ascending order by id.

Args:
    username (str): The username for the MySQL database.
    password (str): The password for the MySQL database.
    database (str): The name of the MySQL database containing the 'states'

Details:
    - Establishes a connection to the MySQL database on localhost at port 3306.
    - Utilizes SQLAlchemy to query all State objects from the 'states' table.
    - Results are sorted in ascending order by the State's id.
    - Each State object is printed in the format "{id}: {name}".
    - The session with the database is closed
    after retrieving and printing the results.

Example usage:
    $ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
    1: California
    2: Arizona
    3: Texas
    4: New York
    5: Nevada
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
