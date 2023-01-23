first = map(int, input().split())
numbers = list(first)
def filter_prime(n):
    for i in n:
        mm = True
        for j in range(2, i):
            if i % j == 0:
                mm = False
        if mm and i != 1 and i != 0:
            print(i, end = " ")
filter_prime(numbers)