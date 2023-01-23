set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)

try:
    set1.remove(10)
except Exception as e:
    print("Error" + str(e) )
print(set1)
print("Hello world")
