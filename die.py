from random import randint

class Die():
    """Klasa przedstawiająca pojedynczą kość z gry"""
    def __init__(self, num_sides=6):
        """Sześcian"""
        self.num_sides = num_sides
        
    def roll(self):
        """od 1 do l.ścianek kości"""
        return randint(1, self.num_sides)
