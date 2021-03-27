#!/usr/bin/python3
"""
    Script that lists all cities from the database.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=db)
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
             FROM cities LEFT JOIN states \
             ON states.id = cities.state_id ORDER BY cities.id ASC;"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
