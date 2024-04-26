import sqlite3
import json
import os

def handle_vote(data):
    with open("vote.json","r") as vote:
        json.dump(data, vote)
    result_value = data['result']
    name, party = result_value.split(' ', 1)



    with open('uid.txt', 'r') as file:
        line = file.readline()
        values = line.split(',')
        uid = values[0].strip()
        constitution = values[1].strip()
    return name,party,uid,constitution



def vote_cast(constitution, party,uid):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, 'voters.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    table_name = f"{constitution}_CANDIDATES"
    c.execute(f"UPDATE {table_name} SET votes = votes + 1 WHERE party = ?", (party,))
    c.execute("INSERT INTO voted (uid) VALUES (?)", (uid,))
    conn.commit()
    conn.close()
