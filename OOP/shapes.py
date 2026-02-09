class Shape:

    def area(self):
        print("Shape: N/A")


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height


rect = Rectangle(4, 5)
rect.area()

sp = Shape()
sp.area()
