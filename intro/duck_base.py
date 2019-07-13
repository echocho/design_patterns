from abc import abstractmethod


class DuckBaseType(object):
    def __init__(self):
        self.name = 'base type of duck'

    def display(self):
        print(f"I'm {self.name}")

    @staticmethod
    def swim():
        print("I'm swimming")

    @abstractmethod
    def fly(self):
        raise NotImplementedError

    @abstractmethod
    def quack(self):
        raise NotImplementedError
