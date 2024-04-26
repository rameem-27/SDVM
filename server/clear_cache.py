import os

def swipe():
    try:
        def delete_contents(directory):
            for root, dirs, files in os.walk(directory, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))

        static_folder = "static"
        if os.path.exists(static_folder) and os.path.isdir(static_folder):
            delete_contents(static_folder)

        folder_path = os.getcwd()
        files = os.listdir(folder_path)
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
    except Exception as e:
        return "Error occurred: {}".format(e)

