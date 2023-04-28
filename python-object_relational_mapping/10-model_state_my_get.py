#!/usr/bin/python3
"""A script that prints the state object with the\
        name passed as an argument"""

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
    data = session.query(State).filter(State.name == "{}".format(
        sys.argv[4])).all()

    if data:
        for record in data:
            if record.name == sys.argv[4]:
                print("{}".format(record.__dict__['id']))
    else:
        print("Not found")

    session.close()
