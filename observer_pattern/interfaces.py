from abc import ABCMeta, abstractmethod


class SubjectInterface(object):
    def __init__(self):
        self.observers = []

    def register_observer(self, observer: 'ObserverInterface'):
        self.observers.append(observer)

    def remove_observer(self, observer: 'ObserverInterface'):
        if self.observers:
            self.observers.remove(observer)

    @abstractmethod
    def notify_observers(self, **kwargs):
        pass


class ObserverInterface(object):
    __meta__ = ABCMeta

    @staticmethod
    def update(self, temperature, humidity, pressure):
        raise NotImplementedError('Need a concrete class to implement this')


class DisplayElementInterface(object):
    __meta__ = ABCMeta

    @staticmethod
    def display(self):
        raise NotImplementedError('Need a concrete class to implement this')
