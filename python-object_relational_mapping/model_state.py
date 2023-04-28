#!/usr/bin/python3
"""A python file that contains the class def.\
        of a state and an instance Base"""

import sqlalchemy
from sqlalchemy import column, integer, string
from sqlalchemy.ext.declarative import declarative_base

Base= declarative_base()


class State(Base):
    """Presents a state"""
    __tablename__ = 'states'
    id = column(Integer, primary_key=True)
    name = column(String(128),nullabel=False)
