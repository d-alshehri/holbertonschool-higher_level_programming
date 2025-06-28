#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extract arguments
    username, password, db_name, state_name = sys.argv[1:5]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    # Secure query with parameterization (SQL injection safe)
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    # Join city names into comma-separated string
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
