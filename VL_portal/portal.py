from flask import Flask, render_template, request, redirect ,url_for, flash
from aadhaar_search import search_aadhaar
from aadhaar_jinja import jinja_aadhaar
from voter_search import search_voter
from voter_jinja import jinja_voter
from data import extract_all_data
import subprocess
import sqlite3
import json
import os

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def delete_json_files():
    files = os.listdir()
    for file in files:
        if file.endswith('.json'):
            os.remove(file)



@app.route('/')
def root():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    error=''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(root_dir, 'credentials.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM credentials WHERE username=?", (username,))
        queried_data = cursor.fetchone()
        if queried_data and password == queried_data[0]:
            return redirect(url_for('home'))
        else:
            flash('Wrong email or password')
            return redirect(url_for('login'))
    return render_template('login.html')



@app.route('/home', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        uid_value = request.form['searchInput']
        x = search_voter(uid_value)
        if x == True:
            return jinja_voter(uid_value)
        elif x == False:
            y = search_aadhaar(uid_value)
            return jinja_aadhaar(uid_value)
    else:
        return render_template('home.html')
    
    
    
@app.route('/remove', methods=['POST'])
def removing_voter():
    if request.method == 'POST':
        data = request.json
        uid_value = data.get('uid_value')
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(root_dir, 'voters.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM list WHERE uid=?", (uid_value,))
        conn.commit()
        conn.close()

    return render_template('home.html')



    
@app.route('/add',methods=['POST','GET'])
def adding_voter():
    if request.method == 'POST':
        data = request.json
        uid_value = data.get('uid_value')
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        adb_path = os.path.join(root_dir, 'aadhaar.db')
        aadhaar_conn = sqlite3.connect(adb_path)
        aadhaar_cursor = aadhaar_conn.cursor()
        aadhaar_cursor.execute(f"SELECT * FROM details WHERE uid={uid_value}")
        result = aadhaar_cursor.fetchone()
        uid = result[0]
        name = result[1]
        gender = result[2]
        co = result[3]
        house = result[4]
        loc =result[5]
        yob = result[7]
        aadhaar_conn.close()
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        vdb_path = os.path.join(root_dir, 'voters.db')
        voters_conn = sqlite3.connect(vdb_path)
        voters_cursor = voters_conn.cursor()
        voters_cursor.execute('INSERT INTO list (uid, name, gender,co, house, yob, loc) VALUES (?,?,?,?,?,?,?)', (uid,name,gender,co,house,yob,loc))
        voters_conn.commit()
        voters_conn.close()
    return render_template('home.html')       
        




@app.route('/result')
def result():
    subprocess.run(["python3","result.py"])
    all_data = extract_all_data()
    delete_json_files()
    with open('result.json', 'w') as json_file:
        json.dump(all_data, json_file)
        
    with open('result.json', 'r') as j:
        result = json.load(j)
    C1party1 = result.get('Aparty1')

    C1party2 = result.get('Aparty2')

    C1percentage1 = result.get('Apercentage1')

    C1percentage2 = result.get('Apercentage2')

    C2party1 = result.get('Bparty1')

    C2party2 = result.get('Bparty2')

    C2percentage1 = result.get('Bpercentage1')

    C2percentage2 = result.get('Bpercentage2')

    
    
    return render_template('constitution_result.html',C1party1=C1party1,C1party2=C1party2,C1percentage1=C1percentage1,
                           C1percentage2=C1percentage2,C2party1=C2party1,C2party2=C2party2,C2percentage1=C2percentage1,C2percentage2=C2percentage2)




    


if __name__ == '__main__':
    app.run(debug=True)