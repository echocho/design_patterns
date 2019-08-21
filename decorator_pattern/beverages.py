from abc import ABC, abstractmethod
from enum import Enum

from decorator_pattern.exceptions import SizeNotDefineError


class Size(Enum):
    TALL = 0.10
    GRANDE = 0.15
    VENTI = 0.20


class Beverage(ABC):
    def __init__(self):
        self.description = 'Unknown Beverage'

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        raise NotImplementedError('Need concrete implementation')

    @abstractmethod
    def get_size(self):
        raise NotImplementedError('Need concrete implementation')

    @abstractmethod
    def set_size(self, size: Size):
        raise NotImplementedError('Need concrete implementation')


class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.description = 'Espresso'
        self.size = None
        self.coffee_cost = 1.99

    def cost(self):
        return self.coffee_cost + self.get_size().value

    def set_size(self, size: Size):
        self.size = size

    def get_size(self):
        if not self.size:
            raise SizeNotDefineError()
        return self.size


class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = 'House Blend Coffee'
        self.size = None
        self.coffee_cost = 0.89

    def cost(self):
        return self.coffee_cost + self.get_size().value

    def set_size(self, size: Size):
        self.size = size

    def get_size(self):
        if not self.size:
            raise SizeNotDefineError()
        return self.size
