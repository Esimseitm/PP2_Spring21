import os
# os.csandir

def show_files_and_dirs(dir_path: str):
    with os.scandir(dir_path) as scan:
        for entry in scan:
            print(entry.name)

show_files_and_dirs(os.getcwd)