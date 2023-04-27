#!/usr/bin/python3
"""A script that takes in an argument and displays all its values in the database"""
import MySQLdb
import sys


def select_states():
    """Displays all the values of an argument in a database"""

    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2],
                         port=3306, db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE\
            name LIKE BINARY '{:s}'\
            ORDER BY id".format(sys.argv[4]))

    states = cursor.fetchall()
    for states in states:
        print(states)

    cur.close()
    db.close()


if __name__ == "__main__":
    select_states()
