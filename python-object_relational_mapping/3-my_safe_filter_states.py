#!/usr/bin/python3
"""A script that takes in arguments and displays\
        its values in the database"""
import MySQLdb
import sys


def select_states():
    """Displays the values of arguments in the database"""

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE\
            %s ORDER BY id", (sys.argv[4],))

    states = cur.fetchall()
    for states in states:
        print(states)

    cur.close()
    db.close()


if __name__ == "__main__":
    select_states()
