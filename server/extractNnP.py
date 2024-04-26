import json
import os


def extracting():
    files = os.listdir()
    json_files = [file for file in files if file.endswith('.json')]

    if len(json_files) != 2:
        print("Error: There must be exactly two JSON files in the current directory.")
    else:
        with open(json_files[0], 'r') as file1:
            data1 = json.load(file1)
            Name1 = data1.get("Name")
            Party1 = data1.get("Party_Name")


        with open(json_files[1], 'r') as file2:
            data2 = json.load(file2)
            Name2 = data2.get("Name")
            Party2 = data2.get("Party_Name")

    return Name1, Party1, Name2, Party2
