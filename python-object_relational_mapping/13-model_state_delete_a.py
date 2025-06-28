#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states with 'a' in their name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete all those states
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
