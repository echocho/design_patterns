from decorator_pattern.beverages import Beverage, Size


class CondimentDecorator(object):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def cost(self):
        raise NotImplementedError('Need concrete implementation')

    def get_description(self):
        raise NotImplementedError('Need concreate implementation')


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self.beverage = beverage
        self.condiment_cost = 0.2

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self):
        return self.condiment_cost + self.beverage.cost()


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        super().__init__(beverage)
        self.beverage = beverage
        self.condiment_cost = 0.1

    def get_description(self):
        return self.beverage.get_description() + ', Milk'

    def cost(self):
        return self.condiment_cost + self.beverage.cost()
