#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """access and retrieve cities from hbtn_0e_4_usa  database"""
    db_connect = db.connect(host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                            FROM cities JOIN states ON cities.state_id \
                            = states.id ORDER BY cities.id ASC")
    
    sel_rws = db_cursor.fetchall()

    if sel_rws is not None:
        for row in sel_rws:
            print(row)
