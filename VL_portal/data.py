import json
import os

def extract_data(prefix):
    results = {}
    file_paths = [filename for filename in os.listdir() if filename.startswith(prefix)]
    data = [json.load(open(file_path, 'r')) for file_path in file_paths]
    party_keys = [f"{prefix}party{i}" for i in range(1, len(file_paths) + 1)]
    percentage_keys = [f"{prefix}percentage{i}" for i in range(1, len(file_paths) + 1)]

    results.update({party_key: d['Party_Name'] for party_key, d in zip(party_keys, data)})
    results.update({percentage_key: d['percentage'] for percentage_key, d in zip(percentage_keys, data)})

    return results

def extract_all_data():
    all_data = {}
    data_A = extract_data('A')
    data_B = extract_data('B')

    all_data.update(data_A)
    all_data.update(data_B)

    return all_data

