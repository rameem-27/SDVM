import os

def delete_json_files():
    try:
        folder_path = os.getcwd()
        files = os.listdir(folder_path)
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
    except Exception as e:
        return "error in clr_json.py file"
delete_json_files()

os.remove("xml_data.txt")
