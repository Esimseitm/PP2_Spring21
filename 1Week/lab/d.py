a = int(input())
b = input()
if b == 'k':
    c = int(input())
    g = round(a / 1024, c)
    print(g)
else:
    print(a * 1024)

