#!/usr/bin/python3
"""
    Script that lists all states with a name starting with
    N (upper N) from the database.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER \
                    BY id ASC;")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
