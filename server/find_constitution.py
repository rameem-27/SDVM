import sqlite3
import json
import sys

uid_value = sys.argv[1]

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
#check if the place corresponding to uid_value is present in A
    conn = sqlite3.connect('voters.db')
    c = conn.cursor()
    c.execute("SELECT * FROM A WHERE PLACES = ?", (place,))
    result = c.fetchone()
    if result:
        return True
    else:
        return False
    
def search_B(place):
#check if the place corresponding to uid_value is present in B
    conn = sqlite3.connect('voters.db')
    c = conn.cursor()
    c.execute("SELECT * FROM B WHERE PLACES = ?", (place,))
    result = c.fetchone()
    if result:
        return True
    else:
        return False
       
find_constitution(uid_value) 
        