import re

pattern = r'\b\w{3}\b'

text = 'abc defppp k12 lll$    fff mmmm'

print(re.findall(pattern, text))

