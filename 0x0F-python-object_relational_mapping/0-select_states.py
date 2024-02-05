#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """access and retrival of states from databases"""
    db_connect = MySQLdb.connect(host="localhost", port=3306, 
            user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    sel_rws = db_cursor.fetchall()
    
    for row in sel_rws:
        print(row)
