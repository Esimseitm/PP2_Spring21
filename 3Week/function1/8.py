strok = map(int, input().split())
strok = list(strok)

def func(lista):
    arr = []
    for i in lista:
        if i == 0 or i == 7:
            arr.append(i)
    for i in range(len(arr) - 2):
        if arr[i] == 0 and arr[i+1] == 0 and arr[i+2] == 7:
            return True
    return False
print(func(strok))