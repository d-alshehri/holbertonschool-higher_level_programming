#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa with their state names."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extract command-line arguments
    username, password, db_name = sys.argv[1:4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    # SQL JOIN between cities and states
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)

    # Fetch and print all results
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
