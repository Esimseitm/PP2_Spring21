n = int(input())

def chetni(n):
    i = 2
    while i < n:
        yield i
        i += 2

for item in chetni(n):
    print (item, end = ", ")
