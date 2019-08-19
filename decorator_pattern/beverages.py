from abc import ABC, abstractmethod
from enum import Enum


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
