import sqlite3
import json
import os

def find_constitution(uid_value):
    with open(f"{uid_value}_A.json", "r") as f:
        data = json.load(f)
        place = data.get("loc")
        A = search_A(place)
        B = search_B(place)
        if A:
            print("A")
            return "A"
        elif B:
            print("B")
            return "B"
        else:
            return "Neither A or B"
      
def search_A(place):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, 'voters.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM A WHERE PLACES = ?", (place,))
    result = c.fetchone()
    if result:
        return True
    else:
        return False
    
def search_B(place):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, 'voters.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM B WHERE PLACES = ?", (place,))
    result = c.fetchone()
    if result:
        return True
    else:
        return False
