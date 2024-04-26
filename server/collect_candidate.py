import sqlite3
import base64
import json
import os



def candidate_jsons(constitution):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, 'voters.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT DISTINCT Party_Name FROM {constitution}_CANDIDATES")
    party_names = cursor.fetchall()
    for party_name in party_names:
        party_name = party_name[0]
        cursor.execute(f"SELECT * FROM {constitution}_CANDIDATES WHERE Party_Name = ?", (party_name,))
        data = cursor.fetchone()
        json_data = {}
        columns = [description[0] for description in cursor.description]
        for i, column in enumerate(columns):
            if column == "Image" or column == "Symbol":
                image_blob = data[i]
                if image_blob is not None:
                    encoded_image = base64.b64encode(image_blob).decode('utf-8')
                    json_data[column] = encoded_image
                else:
                    json_data[column] = None
            else:
                json_data[column] = data[i]
        file_name = f"{constitution}_{party_name}.json"
        with open(file_name, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
    conn.close()

