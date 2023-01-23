number = list(map(int, input().split()))
bbc = None
s = 0
a = []
if len(number) <= 1:
    bbc = int(input())
if bbc is None:
    bbc = number[1]
number = number[0]
for i in range(0,number):
    a.append(bbc + 2*i)
    s ^=a[i]
print(s)