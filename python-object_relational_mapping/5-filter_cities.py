#!/usr/bin/python3
"""A script that takes in the name of a state as an argument"""
import MySQLdb
import sys


def my_safe_filter_states():
    """Takes in the name of the state as an\
            argument and lists all cities"""

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], port=3306, db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states\
            ON cities.state_id = states.id WHERE states.name\
            LIKE %s ORDER BY cities.id", (sys.argv[4]))

    cities = cur.fetchall()
    for cities in cities:
        cities.append(cities[0])
    print(", ".join(cities))
    cur.close()
    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
