import re

text = input()

pattern = r'[a-z]+_[a-z]+'

x = re.findall(pattern, text)
print(x)