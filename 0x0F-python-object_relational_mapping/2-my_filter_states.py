#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states 
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
from sys import argv

if __name__ = '__main__':
    """
    access and retrieve the states from the database
    """
    db_connect = db.connect(host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
            states.id ASC".format(argv[4]))
    sel_rws = db_cursor.fetchall()

    for row in sel_rws:
        print(row)
