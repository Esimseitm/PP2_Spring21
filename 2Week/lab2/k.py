ab = input() 
set=set() 
list=list() 
aa = 0 
pow = ""
for i in range(len(ab)) : 
    if ab[i]!=" " : 
        if ab[i] >= 'A' and ab[i] <= "z": 
            pow = pow + ab[i] 
    if ab[i] == " ": 
        set.add(pow) 
        pow = "" 
    if i == len(ab)-1: 
        if pow != "": 
            set.add(pow) 

for i in set: 
    list.append(i) 
    aa = aa + 1 

list.sort() 
print(aa) 
for i in list : 
    print(i)