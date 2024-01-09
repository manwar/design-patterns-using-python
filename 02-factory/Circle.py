from Shape import Shape

class Circle(Shape):
    def area(self, radius):
        return 3.14 * (radius ** 2)
