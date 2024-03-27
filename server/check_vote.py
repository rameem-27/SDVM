import sqlite3




def check(uid_value):
    with sqlite3.connect('voters.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM voted WHERE uid = ?", (uid_value,))
        row = cursor.fetchone()
        if row:
            return True
        else:
            return False
