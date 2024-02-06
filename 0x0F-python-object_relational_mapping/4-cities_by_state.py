#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """access and retrieve cities from hbtn_0e_4_usa  database"""
    db_connect = db.connect(host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3])

    my_cursor = db.cursor()
    my_cursor.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON state_id = cities.states_id ORDER BY cities.id ASC")
    
    sel_rws = my_cursor.fetchall()

    for row in sel_rws:
        print(row)
    my_cursor.close()
    db.close()
