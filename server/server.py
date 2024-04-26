from clear_cache import swipe
swipe()
from flask import Flask, render_template, request, jsonify
from aadhaar_check import query_aadhaar, compare_aadhaar_jsons
from voter_ckeck import query_voter, compare_voter_jsons
from find_constitution import find_constitution
from collect_candidate import candidate_jsons
from saving_images import images
from extractNnP import extracting
from toJson import xml
import sqlite3
import json
import os


app = Flask(__name__)    

@app.route('/verification',methods=["POST"])
def index():
    swipe()
    if request.method == 'POST':
        data = request.form.get("data")
        data_string = data.replace("'", "\"")
        data = json.loads(data_string)
        print(data)
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=2)
        uid = xml()
        with open("uid.txt","w") as f:
            f.write(uid)
            
        if check_if_voted(uid) == False:    
            if verification_aux(uid,True) == False:
                return render_template("aadhaar_fail.html")
            if verification_aux(uid,False) == False:
                return render_template("voter_fail.html")
            
            return render_template("verify_fingerprint.html")

        else:
            return render_template('already_voted.html')
    return render_template("scan_again.html")



@app.route("/voting", methods=['GET'])
def voting():
    with open("uid.txt", "r") as file:
        uid = file.read()
    
    constitution = find_constitution(uid)
    with open("uid.txt","w") as f:
        f.write(f"{uid},{constitution}")
                    
        if os.path.exists(f"{uid}_A.json"):
            os.remove(f"{uid}_A.json")
        if os.path.exists(f"{uid}_V.json"):
            os.remove(f"{uid}_V.json")
        candidate_jsons(constitution)
        images()
        Name1, Party1, Name2, Party2 = extracting()                   
        box1_image = f"/static/{constitution}_{Party1}/{Name1}.png"
        box2_image = f"/static/{constitution}_{Party1}/{Party1}.png"
        box5_image = f"/static/{constitution}_{Party2}/{Name2}.png"
        box6_image = f"/static/{constitution}_{Party2}/{Party2}.png"
        box3_text = f"{Name1}    {Party1}"
        box7_text = f"{Name2}    {Party2}"
            
        return render_template('voting_interface.html', box1_image=box1_image, box2_image=box2_image,
                                    box5_image=box5_image, box6_image=box6_image,
                                    box3_text=box3_text, box7_text=box7_text)


@app.route('/asd', methods=['POST'])
def handle_verification():
    data = request.json
    result_value = data['result']
    name, party = result_value.split(' ', 1) 
    with open('uid.txt', 'r') as file:
        line = file.readline()
        values = line.split(',')
        uid = values[0].strip()
        constitution = values[1].strip()
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(root_dir, 'voters.db')
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        table_name = f"{constitution}_CANDIDATES"
        c.execute(f"UPDATE {table_name} SET votes = votes + 1 WHERE Party_Name = ?", (party,))
        c.execute("INSERT INTO voted (uid) VALUES (?)", (uid,))
        conn.commit()
        conn.close()
    return "OKK"

@app.route('/redirect',methods=['GET'])
def redirect():
    return render_template('your_vote.html')


def verification_aux(uid,isAdhaar):
    if isAdhaar:
        filename1 = f"{uid}_A.json"
        filename2 = f"{uid}_QA.json"
        query_func = query_aadhaar
        compare_func = compare_aadhaar_jsons
    else:
        filename1 = f"{uid}_V.json"
        filename2 = f"{uid}_QV.json"
        query_func = query_voter
        compare_func = compare_voter_jsons
        
    if query_func(uid) == True:
                        
        if compare_func(filename2,filename1) == True:
            os.remove(filename2)
            return True
        else:
            return False
    else:
        return False



def check_if_voted(uid):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, 'voters.db')
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM voted WHERE uid = ?", (uid,))
        row = cursor.fetchone()
        if row:
            return True
        else:
            return False


        
def get_json_files():
    json_files = {}
    directory = os.getcwd()
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), 'r') as file:
                file_content = file.read()
                json_files[filename] = file_content
    return jsonify(json_files)



    
if __name__ == '__main__':
    app.run(port=8080,debug=True)
