"""
Template method pattern defines the skeleton of an algorithm in an method,
deferring some steps to subclasses. Template Method lets subclasses redefine
certain steps of an algorithm without changing the the algorithm's structure.

Hook: a method in the abstract superclass that does nothing or provides default
behavior.

The steps in the algorithm that must be supplied by the subclasses are usually
declared as abstract. Can be overridden in subclasses.

The Hollywood principle: Don't call us, we'll call you. Put decision making in
high-level modules that can decide how and when to call low-level modules.
"""
from abc import abstractmethod, ABCMeta


class CaffeineBeverage(object):
    __metaclass__ = ABCMeta

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.need_condiments():
            self.add_condiments()

    @staticmethod
    def boil_water():
        print("Boiling water ...")

    @abstractmethod
    def brew(self):
        raise NotImplementedError()

    @staticmethod
    def pour_in_cup():
        print("Pouring into a cup ...")

    @abstractmethod
    def add_condiments(self):
        raise NotImplementedError()

    def need_condiments(self):
        response = input('Would you like sugar and milk in your coffee? ')
        if response.lower().startswith('y'):
            return True
        return False


class Coffee(CaffeineBeverage):
    def brew(self):
        print("Brewing coffee grinds")

    def add_condiments(self):
        print("Adding sugar and milk into coffee")


class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping tea bag ...")

    def add_condiments(self):
        print("Adding lemon to tea ...")


coffee = Coffee()
coffee.prepare_recipe()

tea = Tea()
tea.prepare_recipe()
