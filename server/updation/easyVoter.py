import xmltodict
import sqlite3
import json
import sys
import os

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print("File not found:", filename)
        sys.exit(1)
        
def to_json(file_data):
    xml_data = file_data.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
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
    selected_keys = ['uid', 'name', 'gender', 'co', 'house','yob', 'loc']
    aadhaar_data = {key: final_data[key] for key in selected_keys if key in final_data}
    with open('update.json', 'w') as aadhaar_json_file:
        json.dump(aadhaar_data, aadhaar_json_file, indent=2)    
    if os.path.exists('data.json'):
        os.remove('data.json')
        
        
def insert_into_voters_db():
    with open('update.json', 'r') as json_file:
        data = json.load(json_file)
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, 'voters.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    keys = list(data.keys())
    values = [data[key] for key in keys]
    columns = ', '.join(keys)
    placeholders = ', '.join(['?' for _ in range(len(keys))])
    insert_query = f"INSERT INTO list ({columns}) VALUES ({placeholders})"
    try:
        c.execute(insert_query, values)
        conn.commit()
    except sqlite3.IntegrityError:
        print("Error: UNIQUE constraint failed. Data already exists in the database.")
        conn.rollback()
        sys.exit(1)
    finally:
        conn.close()
        
def remove_frm_voters_db():
    with open('update.json', 'r') as json_file:
        data = json.load(json_file)
        first_key = next(iter(data))
        uid_value = f"{data[first_key]}"
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, 'voters.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("DELETE FROM list WHERE uid = ?", (uid_value,))
    conn.commit()
    conn.close()
    
def remove():
    if os.path.exists("update.json"):
        os.remove("update.json")

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py -a/-r filename.txt")
        sys.exit(1)
    
    option = sys.argv[1]
    filename = sys.argv[2]

    if option == '-a':
        file_data = read_file(filename)
        to_json(file_data)
        insert_into_voters_db()
        remove()
        
    elif option == '-r':
        file_data = read_file(filename)
        to_json(file_data)
        remove_frm_voters_db()
        remove()

    else:
        print("Invalid option. Please use '-a' or '-r'.")
        sys.exit(1)

if __name__ == "__main__":
    main()