import sqlite3
conn = sqlite3.connect('voters.db')
c = conn.cursor()
c.execute('''
        CREATE TABLE list(
        uid int primary key,
        name char,
        gender char,
        co char,
        house char,
        yob int)
            ''');
conn.commit()