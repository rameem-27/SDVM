import sqlite3
import os
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(root_dir, 'voters.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()
# c.execute('''
# INSERT INTO list(uid, name, gender, co, house, yob)      
      
#         VALUES('902303297567', 'Muhammed Rameem M A', 'M', 'S/O Abdul Azeez M A', 'Mundackal House', '2002')

#           ''');


# # conn.execute("UPDATE list SET co = x WHERE name = y ")

#c.execute("UPDATE B_CANDIDATES SET votes = 0;")

# conn.commit()