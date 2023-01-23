a = int(input())
max = -100000
ab = {}
summa = 0
for i in range(a):
    ss,sum = map(str,input().split())
    sum = int(sum)
    if ss not in ab:
        ab[ss] = sum
    else:
        summa = ab[ss] + sum
        ab[ss] = summa
        sum = summa
    if sum > max:
        max = sum
su = 0
for one, two in sorted(ab.items()):
    if two != max:
        su = max - two
        two = su
        print(one + " has to receive " + str(two) + " tenge ")
    else:
        print(one + " is lucky!")