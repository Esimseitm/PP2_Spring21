import re

text = 'test 19.01.2018 as;as;ds;dfbdfsdf  01.09.2017'

for i in re.finditer(r'\d\d.\d\d.\d{4}' , text):
    print('Дата', i[0], 'начинается с позиции', i.start())