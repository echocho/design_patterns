from decorator_pattern.beverages import Beverage, Size


class CondimentDecorator(Beverage):
    def cost(self):
        raise NotImplementedError('Need concrete implementation')

    def get_size(self):
        raise NotImplementedError('Need concrete implementation')

    def set_size(self, size: Size):
        raise NotImplementedError('Need concrete implementation')


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self):
        return 0.2 + self.beverage.cost()


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage
        self.size = None

    def get_description(self):
        return self.beverage.get_description() + ', Milk'

    def set_size(self, size: Size):
        self.size = size

    def cost(self):
        return 0.1 + self.beverage.cost()
