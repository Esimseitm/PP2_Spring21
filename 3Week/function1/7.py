three = map(int, input().split())
three = list(three)

def func(lista):
    if 3 in lista:
        for i in range(len(lista) - 1):
            if lista[i] == 3 and lista[i+1] == 3:
                return True
        return False
    else:
        return False
print(func(three))