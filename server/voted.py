import sqlite3
import os

uid = 902303297567


def voted(uid):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, 'voters.db')
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO voted (uid) VALUES (?)", (uid,))
            
            
        
def remove_voted(uid):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, 'voters.db')
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM voted WHERE uid = ?", (uid,))



def clear_voted():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, 'voters.db')
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS voted")
        cursor.execute("CREATE TABLE IF NOT EXISTS voted (uid TEXT)")
        cursor.execute("UPDATE B_CANDIDATES SET votes = 0;")
        cursor.execute("UPDATE A_CANDIDATES SET votes = 0;")


#voted(uid)
#remove_voted() 
clear_voted()