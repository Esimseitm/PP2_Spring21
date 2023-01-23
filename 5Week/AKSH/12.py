import re

file = open("raw.data", 'r', encoding="utf-8")
text = file.read()

pattern = r'\nБИН.*(?P<BIN>\b[0-9]+)\nНДС.*(?P<NDS>\b[0-9]+)'

x = re.compile(pattern)

for match in x.finditer(text):
    print(match)

file.close()