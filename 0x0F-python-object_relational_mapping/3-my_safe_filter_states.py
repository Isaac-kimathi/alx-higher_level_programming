#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa 
where name matches the argument and that is safe from MySQL injections
"""

import MySQLdb as db
from sys import argv

if __name__ == '__name__':
    """access and retrieve states from the database"""
    db_connect = db.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    sel_rws = db_cursor.fetchall()

    for row in sel_rws:
        print(row)
