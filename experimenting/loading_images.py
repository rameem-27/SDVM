import os

def print_files_in_folders(folder_suffix):
    cwd = os.getcwd()
    for root, dirs, files in os.walk(cwd):
        for dir_name in dirs:
            if dir_name.endswith(folder_suffix):
                folder_full_path = os.path.join(root, dir_name)
                print(f"Files in folder '{folder_full_path}':")
                for file_name in os.listdir(folder_full_path):
                    print(file_name)

folder_suffix_1 = "_1"
folder_suffix_2 = "_2"

print_files_in_folders(folder_suffix_1)
print_files_in_folders(folder_suffix_2)
