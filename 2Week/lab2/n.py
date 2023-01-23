ch = 122398455
ab = []
while ch != 0:
    ch=int(input())
    ab.append(ch)
ab.pop()
am = []
len = len(ab)

if len % 2 == 0:
    for i in range(len//2):
        sum = ab[i] + ab[len - i - 1]
        print(sum, end =" ")
else:
    for i in range(len//2):
        sum = ab[i] + ab[len - i - 1]
        print(sum, end=" ")
    sum2 = ab[len//2]
    print(sum2, end=" ")