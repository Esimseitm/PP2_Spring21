# regex

import re

#pattern = r'\d{5}'
#text = 'test 12345 bbb12341234'

#match = re.search(pattern, text) # ищет первый вхождение

pattern = r'[3-7]{5}' 
text = 'test 34567 bbb12341234'


l = re.findall(pattern, text)

print(l)





