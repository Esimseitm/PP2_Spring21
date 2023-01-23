a, b = map(int,input().split())

if b % 2 == 0 and a <= 500:
    c = 10
    for i in range(2, a):
        if a % i == 0:
            c = 100
    if c == 10:
        print("Good job!")
    else:
        print("Try next time!")
else:
    print("Try next time!")