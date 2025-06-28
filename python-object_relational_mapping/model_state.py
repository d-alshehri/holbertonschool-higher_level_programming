#!/usr/bin/python3
"""
Contains the class definition of a State and an instance of Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create Base class for all ORM classes to inherit from
Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table `states`
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
