#!/usr/bin/python3
"""A script that lists all states"""
import MySQLdb
import sys


def select_states():
    """Lists all states in the database"""

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()

    for states in states:
        print(states)
    cur.close()
    db.close()


if __name__ == "__main__":
    select_states()
