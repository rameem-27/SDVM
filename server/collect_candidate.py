import sqlite3
import base64
import json
import sys

constitution = sys.argv[1]


def candidate_jsons(constitution):
    conn = sqlite3.connect('voters.db')
    cursor = conn.cursor()
# Fetch all unique party names from the database
    cursor.execute(f"SELECT DISTINCT Party_Name FROM {constitution}_CANDIDATES")
    party_names = cursor.fetchall()
# Iterate over each party name and create JSON file
    for party_name in party_names:
        party_name = party_name[0]  # Unpack the tuple
    # Execute the query to fetch data for the current party name
        cursor.execute(f"SELECT * FROM {constitution}_CANDIDATES WHERE Party_Name = ?", (party_name,))
        data = cursor.fetchone()
    # Create a dictionary to store the data
        json_data = {}
    # Loop through the columns and store the values
        columns = [description[0] for description in cursor.description]
        for i, column in enumerate(columns):
        # Convert images to base64
            if column == "Image" or column == "Symbol":
                image_blob = data[i]
                if image_blob is not None:
                    encoded_image = base64.b64encode(image_blob).decode('utf-8')
                    json_data[column] = encoded_image
                else:
                    json_data[column] = None
            else:
                json_data[column] = data[i]
    # Create the JSON file
        file_name = f"{constitution}_{party_name}.json"
        with open(file_name, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        print(f"JSON file '{file_name}' has been created successfully.")
# Close the connection
    conn.close()

candidate_jsons(constitution)