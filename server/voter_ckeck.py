import sqlite3
import json
import os

def query_voter(uid_value):
    try:
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        db_path = os.path.join(root_dir, 'voters.db')
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM list WHERE uid = ?", (uid_value,))
            row = cursor.fetchone()

            if row:
                result_dict = dict(zip([desc[0] for desc in cursor.description], row))

                for key, value in result_dict.items():
                    if isinstance(value, (int, float)):
                        result_dict[key] = str(value)

                with open(f"{uid_value}_QV.json", 'w') as result_file:
                    json.dump(result_dict, result_file, indent=2)
                return True
            else:
                return False

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False



def compare_voter_jsons(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    if isinstance(data1, dict) and isinstance(data2, dict):
        if all(item in data2.items() for item in data1.items()):
            return True
        else:
            return False
    else:
        print("Error: Both files should contain JSON objects.")
