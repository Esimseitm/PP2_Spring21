import os
#os.rename(path1, path2)
# os.makedirs(path)

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def safe_rename(path1, path2):
    if os.path.exists(path1):
        os.rename(path1. path2)

def safe_rmdir(path):
    if os.path.exists(path):
        os.rmdir(path)

#os.makedirs('dir3/dir3_1/dir3_1_1')

#create_dir('new_dir1')
#os.rename('input.txt', 'input_new.txt')
#os.rename('dir1', 'dir1_new')