#!/usr/bin/python3
""" Script that lists all 'states' from the a database """
import MySQLdb
from sys import argv

if __name__ == '__main__':

    data_base = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=data_base)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
