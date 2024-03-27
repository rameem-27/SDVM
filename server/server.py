from flask import Flask, request
from aadhaar_check import query_aadhaar, compare_aadhaar_jsons
from voter_ckeck import query_voter, compare_voter_jsons
import json
import os

app = Flask(__name__)
   
def verification_aux(uid,data,isAdhaar):
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
    with open(filename1,"w") as file:
        json.dump(data, file, indent=2)
        
    if query_func(uid) == True:
                        
        #comparing received and queried voter jsons
        if compare_func(filename2,filename1) == True:
            os.remove(filename2)
            return True
        else:
            return False
    else:
        return False
    

@app.route('/verification',methods=["POST"])
def voters():
#functions are called from voter_check.py
    if request.method == 'POST':
        data = request.get_json()
        aadhaar_payload = data.get('aadhaar_data', {})
        voters_payload = data.get('voters_data', {})
        
        if data:  
            uid_value = aadhaar_payload.get('uid')
            if verification_aux(uid_value,aadhaar_payload,True) == False:
                return "AADHAR VERIFICATION FAILED"
            if verification_aux(uid_value,voters_payload,False) == False:
                return "VOTER VERIFICATION FAILED"
            return "VERIFICATION SUCCESSFULL"
    else:
        return "SCAN AGAIN"  

if __name__ == '__main__':
   app.run(port=8080,debug=True)