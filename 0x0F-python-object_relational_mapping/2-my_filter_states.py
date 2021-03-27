#!/usr/bin/python3
""" Script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    passwd = argv[2]
    d_b = argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=d_b)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name='{}' ORDER BY \
                    id ASC;".format(argv[4]))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
