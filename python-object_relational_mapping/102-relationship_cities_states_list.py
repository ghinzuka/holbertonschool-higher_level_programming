#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database), pool_pre_ping=True
    )
    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        results = session.query(City).order_by(City.id).all()

        for city in results:
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    finally:
        session.close()
