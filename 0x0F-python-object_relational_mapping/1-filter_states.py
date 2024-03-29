#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N) 
from the database hbtn_0e_0_usa"""

import MySQLdb as db
from sys import argv

"""
Access to the database and get the states
from the database.
"""

if __name__ == '__main__':
    """Access and relieve  states from databases"""
    db_connect = db.connect(host="localhost", port=3306,
                                            user=argv[1], passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    sel_rws = db_cursor.fetchall()

    for row in sel_rws:
        print(row)
