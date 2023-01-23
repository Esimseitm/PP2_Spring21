a = int(input())
b = []
for i in range(a):
    string = input()
    if "gmail.com" in string:
        print(string[:-10])
