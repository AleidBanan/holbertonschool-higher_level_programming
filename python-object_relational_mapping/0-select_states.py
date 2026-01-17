#!/usr/bin/python3
"""Lists all states from a MySQL database"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC;")

    rows = c.fetchall()
    for row in rows:
        print(row)

    c.close()
    db.close()
