n = int(input())
aa = '#'
ab = '.'

a = [[0] * n for i in range(n)]
if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if i < j:
                a[i][j] = ab
            else:
                a[i][j] = aa
else:
    for i in range(n):
        for j in range(n):
            if i + j <= n - 2:
                a[i][j] = ab
            else: a[i][j] = aa
for i in a:
        print(''.join([str(elem) for elem in i]))