from tojson import uid_value
import subprocess
import requests
import json
import os

with open(f"{uid_value}_A.json", 'r') as file:
    aadhaar_payload = json.load(file)

with open(f"{uid_value}_V.json", 'r') as file:
    voters_payload = json.load(file)

combined_payload = {"aadhaar_data": aadhaar_payload, "voters_data": voters_payload}

response = requests.post('http://127.0.0.1:8080/verification', json=combined_payload)

print(response.text)


if os.path.exists(f"{uid_value}_A.json"):
    os.remove(f"{uid_value}_A.json")
    
if os.path.exists(f"{uid_value}_V.json"):
    os.remove(f"{uid_value}_V.json")
