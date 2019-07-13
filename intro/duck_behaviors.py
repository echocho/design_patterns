from abc import ABCMeta, abstractmethod


class FlyBehaviorInterface(object):

    __meta__ = ABCMeta

    @abstractmethod
    def fly(self):
        raise NotImplementedError


class QuackBehaviorInterface(object):
    __meta__ = ABCMeta

    @abstractmethod
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehaviorInterface):
    def quack(self):
        print('quacking')


class Squeak(QuackBehaviorInterface):
    def quack(self):
        print('squeaking')


class MuteQuack(QuackBehaviorInterface):
    def quack(self):
        print("I'm mute. I don't quack.")


class FlyWithWings(FlyBehaviorInterface):
    def fly(self):
        print("I'm flying with wings.")


class FlyNoWay(FlyBehaviorInterface):
    def fly(self):
        print("I have no wings. I don't fly.")
