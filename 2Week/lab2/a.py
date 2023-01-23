aa = [int(i) for i in input().split()]

count = 2
manek = 0
manek1 = 0
while manek < len(aa):
    if manek > manek1:
        count = 0
        break
    if manek + aa[manek] > manek1:
        manek1 = manek + aa[manek]
    if manek1 >= len(aa) - 1:
        count = 1
        break
    manek = manek + 1
if count == 1:
    print(1)
else:
    print(0)
