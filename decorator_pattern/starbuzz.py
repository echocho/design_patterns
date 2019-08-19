from decorator_pattern.beverages import Beverage, Size
from decorator_pattern.condiments import Mocha, Milk


class Espresso(Beverage):
    def __init__(self):
        self.description = 'Espresso'
        self.size = None

    def cost(self):
        return 1.99 + self.get_size().value

    def set_size(self, size: Size):
        self.size = size

    def get_size(self):
        # GRANDE size by default
        if self.size:
            return self.size
        self.set_size(Size.GRANDE)
        return self.size


class HouseBlend(Beverage):
    # GRANDE size by default
    def __init__(self):
        self.description = 'House Blend Coffee'
        self.size = None

    def cost(self):
        return 0.89 + self.get_size().value

    def set_size(self, size: Size):
        self.size = size

    def get_size(self):
        if self.size:
            return self.size
        self.set_size(Size.GRANDE)
        return self.size


espresso = Espresso()
print('espresso cost', espresso.cost())
espresso.set_size(Size.GRANDE)
print('espresso with size grande cost', espresso.cost())
espresso_w_milk = Milk(espresso)
print('espresso with milk cost', espresso_w_milk.cost())
house_blend = HouseBlend()
print('house blend cost', house_blend.cost())
house_blend_mocha = Mocha(house_blend)
print('house blend mocha cost', house_blend_mocha.cost())
house_blend.set_size(Size.VENTI)
house_blend_mocha_venti = Mocha(house_blend)
print('venti house blend mocha cost', house_blend_mocha_venti.cost())

