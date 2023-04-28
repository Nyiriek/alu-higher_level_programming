#!/usr/bin/python3
"""A script that lists all cities from a database"""
import MySQLdb
import sys


def select_cities():
    """Lists all cities in a database"""

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], port=3306, db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states ON\
            cities.state_id = states.id ORDER BY cities.id")

    states = cur.fetchall()
    for states in states:
        print(states)

    cur.close()
    db.close()


if __name__ == "__main__":
    select_cities()
