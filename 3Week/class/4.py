class Points:
    def init(self, x, y):
        self.res = ' '
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self):
        self.x = self.x + razmer
        self.y = self.y + razmer
    def dist(self):
        self.res = abs(self.y - self.x)
        print(self.res)
x,y = map(int, input().split())
razmer = int(input())
aab = Points(x, y)
aab.show()
aab.move()
print('After moving points to ' + str(razmer) + ' positions we will get: ', end=' ')
aab.show()
print('Distance between this points: ', end='')
aab.dist()