# zadacha naiti skolko raz povtoryaetsa slovo v liste

a = ['hello', 'world', 'hello', 'world', 'hello', 'abc']
d = dict()

for i in a:
    if i not in d:
        d[i] = 0
    d[i] += 1

for key in d:
    print(key, d[key])

for key, value in d.items():
    print(f'{key} ---> {value}')