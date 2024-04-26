import sqlite3
import json
import os

# Function to convert SQLite table to JSON
def sqlite_to_json(db_file, table_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"SELECT Name, Party_Name, votes FROM {table_name}")
    rows = cursor.fetchall()
    columns = ['Name', 'Party_Name', 'votes']
    data = []
    for row in rows:
        data.append(dict(zip(columns, row)))
    conn.close()
    return data

# Function to calculate percentage
def calculate_percentage(data):
    votes_per_candidate = {candidate["Name"]: candidate["votes"] for candidate in data}
    total_votes = sum(votes_per_candidate.values())
    
    # Handle division by zero case
    if total_votes == 0:
        return {name: 0 for name in votes_per_candidate.keys()}
    
    percentage_per_candidate = {name: (votes / total_votes) * 100 for name, votes in votes_per_candidate.items()}
    return percentage_per_candidate

# Function to update JSON file
def update_json_file(json_data, table_name, party_name):
    percentages = calculate_percentage(json_data)
    
    for candidate in json_data:
        candidate["percentage"] = percentages.get(candidate["Name"], 0)
    
    # Name of the JSON file
    json_filename = f"{table_name.split('_')[0]}_{party_name}.json"
    
    with open(json_filename, "w") as f:
        for candidate in json_data:
            json.dump(candidate, f)
            f.write("\n")


# Function to process JSON files in the current directory
def process_json_files_in_cwd():
    cwd = os.getcwd()
    for filename in os.listdir(cwd):
        if filename.endswith("_CANDIDATES.json"):
            json_file = os.path.join(cwd, filename)
            update_json_file(json_file)

# Path to SQLite database
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(root_dir, 'voters.db')

# Connect to database and get table names
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cursor.fetchall()
candidate_tables = [table[0] for table in table_names if table[0].endswith('_CANDIDATES')]
cursor.close()
conn.close()

# Convert tables to JSON and calculate percentages
for table_name in candidate_tables:
    # Fetch data from SQLite table
    json_data = sqlite_to_json(db_path, table_name)
    
    # Iterate over distinct party names
    party_names = set(candidate['Party_Name'] for candidate in json_data)
    for party_name in party_names:
        # Filter data by party name
        party_data = [candidate for candidate in json_data if candidate['Party_Name'] == party_name]
        update_json_file(party_data, table_name, party_name)

process_json_files_in_cwd()
