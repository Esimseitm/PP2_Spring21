a = input()
brackets = ["[", "(", "{"]
brackets1= ["]", ")", "}"]

list1 = []
count = 0
for i in a:
    if i in brackets:
        list1.append(i)
    else:
            aab = brackets1.index(i)
            if len(list1) != 0 and brackets[aab] == list1[len(list1)-1]:
                list1.pop()
            else:
                count = 1
                break
if count == 0 and len(list1) < 1:
    print("Yes")
else: 
    print("No")