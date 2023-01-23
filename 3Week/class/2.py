class Shape:
    def init(self,length):
        self.length = length
    def area(self):
        print(0)

class Square(Shape):
    def init(self, length):
        self.length = length
    def area(self):
        print(self.length * self.length)

aab = Shape(7)
aab.area()
th = Square(9)
th.area()