#!/usr/bin/python3
"""A script that lists all state objects from the database"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("msql+mysqldb://{}:{}@@localhost/{}".format(sys.argv[1],
                                                                       sys.argv[2],
                                                                       sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    res = session.query(State).all()

    for data in res:
        print("{}: {}".format(data.__dict__['id'], data.__dict__['name']))

    session.close
