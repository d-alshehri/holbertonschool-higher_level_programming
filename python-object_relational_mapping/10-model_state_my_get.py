#!/usr/bin/python3
"""
Print the id of the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Validate the number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State filtered by name, SQL injection safe by using filter()
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
