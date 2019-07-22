from abc import abstractmethod, ABCMeta

"""
The Adapter Pattern converts the interface of a class into another
interface the client expects. Adapter lets the classes work together
that couldn't otherwise because of incompatible interfaces.

There are two types of adapters: `object adapter` and `class adapter`

TurkeyAdapter and DuckAdapter are an example of `object adapter`

"""


class DuckInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def fly(self):
        raise NotImplementedError()

    @abstractmethod
    def quack(self):
        raise NotImplementedError()


class TurkeyInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def gobble(self):
        raise NotImplementedError()

    @abstractmethod
    def fly(self):
        raise NotImplementedError()


class MallardDuck(DuckInterface):
    def fly(self):
        print("I'm flying")

    def quack(self):
        print("Quack")


class WildTurkey(TurkeyInterface):
    def gobble(self):
        print("Gobble")

    def fly(self):
        print("I'm flying, but only a very short distance")


class TurkeyAdapter(DuckInterface):
    """
    Here, Duck is the adapter interface and turkey the adaptee interface
    """
    def __init__(self):
        self.turkey = WildTurkey()

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for _ in range(4):
            self.turkey.fly()


class DuckTestDrive(object):
    def main(self):
        mallard = MallardDuck()
        wild_turkey = WildTurkey()
        print("The wild turkey says ...")
        wild_turkey.gobble()
        print("the mallard say ...")
        mallard.quack()
        print("the wild turkey flies ...")
        wild_turkey.fly()
        print("the mallard flies ...")
        mallard.fly()

    def mock_duck(self):
        mock_duck = TurkeyAdapter()
        print("The mock duck says ...")
        mock_duck.quack()
        print("The mock duck flies ...")
        mock_duck.fly()


DuckTestDrive().main()
DuckTestDrive().mock_duck()
