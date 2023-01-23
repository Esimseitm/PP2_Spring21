import math
def square(n):
    x = 1
    nm1 = 1
    while x <= n:
        number = nm1
        yield number
        x += 1
        nm1 = pow(x , 2)
m = int(input())
for item in square(m):
    print(item, end = " ")