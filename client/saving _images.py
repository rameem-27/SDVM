import json
import base64
import os
import shutil

def save(filename, static_folder):
    with open(filename, "r") as file:
        data = json.load(file)
        name = data.get("Name")
        party = data.get("Party_Name")
        party_symbol = base64.b64decode(data["Symbol"])
        candidate_image = base64.b64decode(data["Image"])

        # Create folder named after JSON filename
        folder_name = os.path.splitext(filename)[0]
        folder_path = os.path.join(static_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Define filenames for images
        party_symbol_filename = os.path.join(folder_path, f"{party}.png")
        candidate_image_filename = os.path.join(folder_path, f"{name}.png")

        # Save images with desired filenames
        with open(party_symbol_filename, "wb") as symbol_file:
            symbol_file.write(party_symbol)

        with open(candidate_image_filename, "wb") as party_file:
            party_file.write(candidate_image)

        return folder_name  # Return the name of the created folder

# Define the folder where the JSON files are located
folder_path = os.getcwd()

# Define the folder where to save the static data
static_folder = os.path.join(folder_path, "static")
if not os.path.exists(static_folder):
    os.makedirs(static_folder)

# Process each JSON file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        created_folder = save(os.path.join(folder_path, filename), static_folder)
        shutil.move(os.path.join(static_folder, created_folder), static_folder)
