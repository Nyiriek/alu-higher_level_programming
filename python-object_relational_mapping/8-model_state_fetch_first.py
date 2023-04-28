#!/usr/bin/python3
"""A script that lists all state objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    data = session.query(State).first()

    if data:
        print("{}: {}".format(data.__dict__['id'], data.__dict__['name']))
    else:
        print("Nothing")

    session.close()
