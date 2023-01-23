def f(n):
    return lambda a: a * n

doubler = f(2)

print(doubler(3))
print(doubler(6))