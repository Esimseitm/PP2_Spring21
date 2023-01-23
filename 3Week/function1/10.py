spisok = map(str, input().split())
spisok = list(spisok)

def dublicat(n):
    arr=[]
    for i in n:
        if not i in arr:
            arr.append(i)
    for i in arr:
        print(i, end = " ")
dublicat(spisok)