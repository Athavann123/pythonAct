class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


a = Point()
a.x = 10
a.y = 20
print(a.x)
a.draw()
