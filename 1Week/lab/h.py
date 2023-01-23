a = input()
c = input()
b = []


gg = 0
ggg= 0
if c in a:
    for i in range(len(a)):
        if c in a[i]:
            gg = i
            break

    ggg = a.rfind(c)
    if gg == ggg:
        print(gg)
    else :
        print(gg,ggg)
