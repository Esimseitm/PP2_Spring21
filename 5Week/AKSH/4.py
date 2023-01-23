import re

text = '7 test +17 ppp -67123 00123'

pattern = r'[+-]?\d+'

print(re.findall(pattern, text))

# functions 
#re.search(pattern, text) # naxodit vse patterni v tekste

#re.fullmatch(pattern, text) - proverka chto stroka podxodit pod pattern
#  re.split(patterm, text) - delaet razbivku texta po patternu
# re.findall(pattern, texxt) - sozdaet massiv patternov v tekste i vivodit ih
# re.finditer(pattern, text) - sozdaet iteratot patterna
# re.sub(pattern, reps text) - po patternu nahodit vse shabloni i zamenayet ix patternom "perl"

