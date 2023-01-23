list1 = list(input().split())


def stroka(lst):
    for i in lst[::-1]:
        print(i, end = " ")
stroka(list1)