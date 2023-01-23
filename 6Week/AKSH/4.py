import os

# pwd - put' k papke
# dir - papka 
# isdir proveryat papka or no
# os.path.exists(path)
# os.remove(path)
# os.path.isdir(path)
# os.path.isfile(path)
# os.rmdir(path) - delete empty papka

path = 'C:/PP2/6week/aksh/input.txt'
path_dir = 'C:/PP2/6week/aksh'
path_to_delete = 'C:/PP2/6week/aksh/dir1'

#if os.path.exists(path):
#    print("yes")
#else:
#    print("NO")

#if os.path.exists(path):
#    os.remove(path)

#if not os.path.isfile(path_dir):
#    print("DIR")
#else:
#    print("File")

# mkdir dir1
# cd dir1
# nano test.txt

os.rmdir(path_to_delete)


