n = int(input())
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
len = len(a)
sum = a[len-2] * a[len-1]
print(sum)