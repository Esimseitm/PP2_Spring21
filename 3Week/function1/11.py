string = input()

def palin(stroka):
    if stroka == stroka[::-1]:
        print("YES, it is palindrom")
    else:
        print("NO, it is not palindrom")
palin(string)