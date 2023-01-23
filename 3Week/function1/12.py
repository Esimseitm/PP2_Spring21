list1 = map(int, input().split())
list1 = list(list1)

def histogram(list1):
    for i in list1:
        for j in range(i):
            print('*', end="")
        print()

histogram(list1)