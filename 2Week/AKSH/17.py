# SCHITIVANIE MASSIVA
#4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

n = int(input())

arr = []

for i in range(n):
    nums = [int(n) for n in input().split(' ')]
    arr.append(nums)
    
for row in arr:
    print(row)