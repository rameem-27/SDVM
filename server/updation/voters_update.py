import sqlite3
conn = sqlite3.connect('voters.db')
c = conn.cursor()
c.execute('''
INSERT INTO list(uid, name, gender, co, house, yob)      
      
        VALUES('902303297567', 'Muhammed Rameem M A', 'M', 'S/O Abdul Azeez M A', 'Mundackal House', '2002')

          ''');
conn.commit()

# conn.execute("UPDATE list SET co = x WHERE name = y ")