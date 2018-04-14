class Hexagon:
    def __init__(self, s):
        self.side = s
    
    def peri(self):
        return self.side * 6
    
hexagon = Hexagon(3)

print(hexagon.peri())