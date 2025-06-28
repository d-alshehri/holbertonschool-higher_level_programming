#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Command-line args: username, password, database
    username, password, db_name = sys.argv[1:4]

    # Create engine and bind it to Base
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session instance
    session = Session()

    # Query all State objects, ordered by id
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    session.close()
