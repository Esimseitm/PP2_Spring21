amm = int(input())
aa = []
cnt = 0
for i in range(amm):
    am = input().split()
    if am[0] == "1":
        st = am[1]
        aa.append(st)
    else:
        cnt += 1

for i in range(cnt):
    print(aa[i], end= " ")
