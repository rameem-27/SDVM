import sqlite3
conn = sqlite3.connect('aadhaar.db')
c = conn.cursor()
c.execute('''
        CREATE TABLE details(
        uid int primary key,
        name char,
        gender char,
        co char,
        house char,
        loc char,
        pc int,
        yob int,
        state char,
        dist char)
            ''');
conn.commit()
