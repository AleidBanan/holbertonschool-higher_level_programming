#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usa
"""
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Create a cursor to execute SQL queries
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306,
                         charset="utf8")
    cur = db.cursor()

    # Execute the query to select all states sorted by id ascending
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display all rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    for state in cur.fetchall():
        print(state)
    cur.close()
    db.close()
