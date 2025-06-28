#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Validate arguments count
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object with name Louisiana
    new_state = State(name="Louisiana")

    # Add and commit the new state to the database
    session.add(new_state)
    session.commit()

    # Print the id of the new state
    print(new_state.id)

    session.close()
