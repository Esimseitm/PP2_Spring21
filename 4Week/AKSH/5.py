# generatots fibonachi

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

a = fib(10)

#print(next(a))
#print(next(a))
#print(next(a))

#print(list(a))
b = list(a)
print(b)