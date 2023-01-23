n = int(input())
ma= 0
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            a[i][j] += ma 
            a[j][i] += ma
        if i == j:
            a[i][j] = ma**2
    ma += 1
for row in a:
    print(' '.join([str(elem) for elem in row]))