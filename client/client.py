from flask import Flask, render_template
import subprocess
import xmltodict
import json
import verify

app = Flask(__name__)

@app.route('/')
def index():
    result = subprocess.check_output(['python3', 'qr_read.py'])
    final_data = result.decode('utf-8')
    if final_data.startswith('<?xml'):
        xml_data = final_data.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
        xml_dict = xmltodict.parse(xml_data)
        data_dict = xml_dict['PrintLetterBarcodeData']
        aadhaar_json = json.dumps(data_dict, indent=4)
        data = json.loads(aadhaar_json)
        uid = data.get('@uid')
        with open("uid.txt","w") as file:
            file.write(uid)
        
        print(data)

        return render_template('index.html', data = data)
    else:
        return render_template('scan_again.html')

@app.route('/fingerprint')
def finger_print_verification():
    uid = ""
    with open("uid.txt", "r") as file:
        uid = file.read()
        print(uid)
    isverified = verify.verify_fingerprint(uid)
    if isverified:
        return render_template('voting.html')
    
    return render_template('fingerprint_failed.html')
    

if __name__ == '__main__':
    app.run(port=5000,debug=True)
