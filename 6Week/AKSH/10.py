import os
import shutil

# shutil.rmtree - удаляет папку со всеми файлами
# shutil.copy - копирует один файл в другой файл
# shutil.copytree - польностю одну папку копировать в другое место
# shutil.move - переместить один файл с одного места в другое

#try:
#    shutil.rmtree('dir3')
#except Exception as e:
#    pass

#shutil.copy('input_new.txt', 'new_dir/test.txt' )

#shutil.copytree('dir2', 'new_dir/dir2_new')

#shutil.move('input_new.txt', 'dir2/')
shutil.move('dir2', 'dir1_new/dir2_test')