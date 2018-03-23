#!/usr/bin/python3
import sys
import MySQLdb


def get_state_safe():
    '''
        List a select state with guard against injection
    '''
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    state_to_find = sys.argv[4]
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_to_find,))
    rows = c.fetchall()
    for i in rows:
        print(i)
    c.close()
    db.close()

if __name__ == "__main__":
    get_state_safe()
