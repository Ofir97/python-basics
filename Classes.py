class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi! I'm {self.name}.")


point1 = Point(10, 20)  # Object - instance of Point
point1.x = 11
print(f'({point1.x},{point1.y})')
print(point1.y)
point1.draw()

point2 = Point(2, 3)
point2.x = 1
print(point2.x)

steve = Person('Steve')
print(steve.name)
steve.talk()

bob = Person('Bob')
bob.talk()


