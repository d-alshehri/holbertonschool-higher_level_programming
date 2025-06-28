#!/usr/bin/python3
"""Script that lists all values in the states table where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extract arguments
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cur = db.cursor()

    # WARNING: vulnerable to SQL injection (we’ll fix this in task 3)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    results = cur.fetchall()
    for row in results:
        print(row)

    # Cleanup
    cur.close()
    db.close()
