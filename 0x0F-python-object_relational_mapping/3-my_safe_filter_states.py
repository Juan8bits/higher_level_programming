#!/usr/bin/python3
""" Script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
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
    query = "SELECT * FROM states WHERE name=%s ORDER BY \
                    id ASC;"
    cursor.execute(query, (state,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
