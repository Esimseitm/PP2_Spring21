b = 10 # Global scope

def hello():
    x = 2 # local scope
    print(b)

    def hi():
        print(x)
    hi()

hello()
print(b)