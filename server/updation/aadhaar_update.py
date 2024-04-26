import sqlite3
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(root_dir, 'aadhaar.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('''
INSERT INTO details(uid, name, gender, co, house, loc, pc, yob, state, dist)

        VALUES('902303297567', 'Muhammed Rameem M A', 'M', 'S/O Abdul Azeez M A', 'Mundackal House', 'Mudickal', '683547', '2002', 'Kerala', 'Ernakulam')

          ''');
conn.commit()


# conn.execute("UPDATE details SET name = x WHERE ID = 222233331111 ")
