class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print("Default area 0")
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(self):
        print(self.length * self.width)

aab = Shape(5, 6)
aab.area()
th = Rectangle(6, 6)
th.area()