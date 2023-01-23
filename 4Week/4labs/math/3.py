import math
n = int(input())
x = int(input())

alp = 180// n
alpha = int(math.tan(alp)) * 2
apothem = x / alpha
p = x * n

s = 0.5 * p * apothem
print(s)