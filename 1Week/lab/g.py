a = input()
sum = 0
d = len(a) -1

for i in a:
    sum += int(i)*2**d
    d -= 1
print(sum)

