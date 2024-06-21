#!/usr/bin/python3
"""
Deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa.

This script connects to a MySQL database specified by command-line arguments,
deletes all State objects from the 'states' table
whose name contains the letter 'a'.

Args:
    username (str): The username for the MySQL database.
    password (str): The password for the MySQL database.
    database (str): The name of the MySQL database
    containing the 'states' table.

Details:
    - Establishes a connection to the MySQL database on localhost at port 3306.
    - Utilizes SQLAlchemy to delete all State objects
    whose name contains the letter 'a'.
    - The session with the database is closed after deleting the state objects.

Example usage:
    $ ./13-model_state_delete_a.py root root hbtn_0e_6_usa
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

    delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in delete:
        session.delete(state)

    session.commit()
    session.close()
