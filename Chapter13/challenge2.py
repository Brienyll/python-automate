class Square():
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        return self.side * 4
    
    def change_size(self, sideChange):
        self.side += sideChange

a_square = Square(15)

print(a_square.calculate_perimeter())

a_square.change_size(-2)

print(a_square.calculate_perimeter())