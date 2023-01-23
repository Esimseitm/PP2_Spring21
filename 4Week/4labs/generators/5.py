n = int(input())

def func(n):
    i = n
    while i > 0:
        yield i
        i -= 1

for item in func(n):
    print(item, end = " ")