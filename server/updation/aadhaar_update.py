import sqlite3
conn = sqlite3.connect('aadhaar.db')
c = conn.cursor()
c.execute('''
INSERT INTO details(uid, name, gender, co, house, loc, pc, yob, state, dist)

        VALUES('902303297567', 'Muhammed Rameem M A', 'M', 'S/O Abdul Azeez M A', 'Mundackal House', 'Mudickal', '683547', '2002', 'Kerala', 'Ernakulam')

          ''');
conn.commit()


# conn.execute("UPDATE details SET name = x WHERE ID = 222233331111 ")
