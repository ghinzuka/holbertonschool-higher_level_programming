#!/usr/bin/python3
"""
Fetches and prints all City objects from the hbtn_0e_14_usa database.

This script connects to a MySQL database specified by command-line arguments,
retrieves all City objects along with their associated states, and prints them
sorted by the city IDs in ascending order.

Arguments:
    - username (str): The username for the MySQL database.
    - password (str): The password for the MySQL database.
    - database (str): The name of the MySQL database
    containing the 'cities' table.

Example Usage:
    $ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(
        State, City.state_id == State.id).order_by(City.id).all()

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
