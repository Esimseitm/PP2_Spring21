import math
a = int(input())
b = int(input())

def square(a, b):
    i = a
    while i < b:
        nm1 = pow(i , 2)
        yield nm1
        i += 1

for item in square(a, b):
    print(item, end = " ")