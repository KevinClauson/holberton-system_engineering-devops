#!/usr/bin/python3
import sys
import MySQLdb


def get_all_states():
    '''
        List all the states in the given database
    '''
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for i in rows:
        print(i)
    c.close()
    db.close()

if __name__ == "__main__":
    get_all_states()
