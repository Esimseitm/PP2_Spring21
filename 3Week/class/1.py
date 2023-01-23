class abcdef:
    def __init__(self):
        self.stroka = " "
    
    def input(self):
        self.stroka = input()

    def print(self):
        print(self.stroka.upper())
        
s = abcdef()
s.input()
s.print()