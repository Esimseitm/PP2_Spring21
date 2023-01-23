n = int(input())

def kratnie(n):
    i = 1
    while i < n:
        if i % 3 == 0 and i % 4 == 0:
            yield i
        i += 1
for item in kratnie(n):
    print(item, end = " ")