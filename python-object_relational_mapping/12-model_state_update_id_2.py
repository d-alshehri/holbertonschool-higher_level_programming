#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Check if arguments count is correct
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state with id=2
    state = session.query(State).filter(State.id == 2).first()

    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
