import json
import os
import sys


def xml():
    with open('data.json','r') as f:
        data = json.load(f)
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


def xml_run():
    with open("xml_data.txt", "r") as f:
        xml_data = f.read()
        if not xml_data.startswith('<?xml'):
            sys.exit("NO")
        else:
            uid_value = xml(xml_data)

