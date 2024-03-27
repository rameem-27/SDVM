import json
import xmltodict
import os
import sys

def xml(xml_data):
    xml_data = xml_data.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
    xml_dict = xmltodict.parse(xml_data)
    data_dict = xml_dict['PrintLetterBarcodeData']
    aadhaar_json = json.dumps(data_dict, indent=4)
    data = json.loads(aadhaar_json)
    old_key = '@gname'
    new_key = '@co'
    old_key_1 = '@lm'
    new_key_1 = '@loc'
    if old_key in data:
        data[new_key] = data.pop(old_key)
        
    if '@loc' not in data and old_key_1 in data:
        data[new_key_1] = data.pop(old_key_1)

    updated_json_data = json.dumps(data, indent=2)

    new_data = json.loads(updated_json_data)

    final_data = {key[1:]: value for key, value in new_data.items()}  

    with open('data.json', 'w') as json_file:
        json.dump(final_data, json_file, indent=2)

    with open('data.json', 'r') as json_file:
        final_data = json.load(json_file)
    
    uid_value = final_data['uid']

    selected_keys = ['uid', 'name', 'gender', 'co', 'house', 'loc', 'pc', 'yob', 'state', 'dist']
    aadhaar_data = {key: final_data[key] for key in selected_keys if key in final_data}
    with open(f"{uid_value}_A.json", 'w') as aadhaar_json_file:
        json.dump(aadhaar_data, aadhaar_json_file, indent=2)

    selected_keys = ['uid', 'name', 'gender', 'co', 'loc', 'house', 'yob',]
    voters_data = {key: final_data[key] for key in selected_keys if key in final_data}
    with open(f"{uid_value}_V.json", 'w') as voters_json_file:
        json.dump(voters_data, voters_json_file, indent=2)
    
    if os.path.exists('data.json'):
        os.remove('data.json')
    
    return uid_value

# Read XML data from file
with open("xml_data.txt", "r") as f:
    xml_data = f.read()
    if not xml_data.startswith('<?xml'):
        sys.exit("NO")
    else:
        uid_value = xml(xml_data)

# Now uid_value can be used outside the function
print("UID Value:", uid_value)
