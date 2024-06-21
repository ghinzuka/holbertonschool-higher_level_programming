#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to
'New Mexico' in the database hbtn_0e_6_usa.

This script connects to a MySQL database specified by command-line arguments,
updates the name of the State object with id = 2 to
'New Mexico' in the 'states' table.

Args:
    username (str): The username for the MySQL database.
    password (str): The password for the MySQL database.
    database (str): The name of the MySQL database
    containing the 'states' table.

Details:
    - Establishes a connection to the MySQL database on localhost at port 3306.
    - Utilizes SQLAlchemy to update the name of the State object with id = 2.
    - The session with the database is closed after updating the state name.

Example usage:
    $ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa
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

    update = session.query(State).filter_by(id=2).first()

    if update:
        update.name = "New Mexico"
        session.commit()

    session.close()
