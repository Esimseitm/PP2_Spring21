import os
# os.getcwd()
# os.chdir(path)

BASE_URL = os.getcwd()

os.chdir('dir1')

with open('new_file.txt', 'w') as f:
    f.write('new file content')


print(BASE_URL)