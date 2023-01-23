a = [1, 2, 3]
b = [4, 5, 6]

c = [ a[i] * b[i] for i in range(len(a))]
print(c)