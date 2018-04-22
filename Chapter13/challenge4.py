class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider
    
class Rider():
    def __init__(self, name):
        self.name = name

Brielle = Rider("Brielle Genna")
animal = Horse("Horsie", Brielle)

print(animal.rider.name)