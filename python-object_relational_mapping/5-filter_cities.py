#!/usr/bin/python3
"""Lists all cities of a given state (SQL injection free)"""

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
    c.execute(
        "SELECT cities.name "
        "FROM cities "
        "INNER JOIN states ON states.id = cities.state_id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;",
        (sys.argv[4],)
    )

    rows = c.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    c.close()
    db.close()
