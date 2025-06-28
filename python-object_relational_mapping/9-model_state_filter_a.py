#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 4:
        return

    user, password, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{db}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # filter states with 'a' in the name, case-insensitive
    states = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

if __name__ == "__main__":
    main()
