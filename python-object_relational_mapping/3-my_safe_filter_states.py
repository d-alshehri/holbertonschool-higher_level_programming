#!/usr/bin/python3
"""Safe script to list states matching a given name (preventing SQL injection)."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get CLI arguments
    username, password, db_name, state_name = sys.argv[1:5]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()
