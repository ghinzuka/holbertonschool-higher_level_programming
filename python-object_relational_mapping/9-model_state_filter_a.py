#!/usr/bin/python3
"""
lists all state objects from the database hbtn_0e_6_usa
that contain the lowercase letter 'a'.

this script connects to a mysql database specified by command-line arguments,
queries all state objects from the 'states' table
where the name contains the lowercase 'a',
and prints each state's id and name in ascending order by id.

args:
    username (str): the username for the mysql database.
    password (str): the password for the mysql database.
    database (str): the name of the mysql database containing
    the 'states' table.

details:
    - establishes a connection to the mysql database on localhost at port 3306.
    - utilizes sqlalchemy to query state objects from the 'states'
    table containing lowercase 'a'.
    - results are sorted in ascending order by the state's id.
    - each state object matching the criteria is printed
    in the format "{id}: {name}".

example usage:
    $ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
    1: california
    2: arizona
    3: texas
    5: nevada
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))

    session.close()
