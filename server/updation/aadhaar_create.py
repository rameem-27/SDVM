import sqlite3
import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(root_dir, 'aadhaar.db')
conn = sqlite3.connect(db_path)
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
