class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square():
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        return self.side * 4

a_rectangle = Rectangle(30, 10)
a_square = Square(15)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())