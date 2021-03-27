#!/usr/bin/python3
"""
    Script that takes in the name of a state as an argument and
    lists all cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    state = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=db)
    cursor = db.cursor()
    query = "SELECT name FROM cities \
             WHERE cities.state_id \
             IN(SELECT id FROM states WHERE name = %s) \
             ORDER BY cities.id"
    cursor.execute(query, (state,))
    i = 0
    for row in cursor.fetchall():
        if (i == 0):
            i += 1
            print(row[0], end="")
        else:
            print(", ", end='')
            print(row[0], end="")
    print()
    cursor.close()
    db.close()
