"""
We are writing a new remote control for TVs. But at this stage, both the remote controls and
TVs are not finalized and we know that they will be changed. So we use bridge pattern, to decouple
abstraction and implementation so that the two can vary independently.
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class TV(object):
    """
    This is the implementation of TV
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def on(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def off(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def tune_channel(self, channel: int):
        raise NotImplementedError(NOT_IMPLEMENTED)


class RemoteControl(object):
    """
    This is the abstraction of our remote control.
    All methods in the abstraction are implemented in terms of the implementation
    """
    def __init__(self, tv_implementor: callable(TV)):
        self.tv = tv_implementor()

    def on(self):
        self.tv.on()

    def off(self):
        self.tv.off()

    def set_channel(self, channel):
        self.tv.tune_channel(channel)

    # and other methods


class ConcreteRemote(RemoteControl):
    """
    Refined abstraction of remote control.
    Concrete subclass are implemented in terms of the abstraction
    """
    def __init__(self, tv: callable(TV)):
        super().__init__(tv)
        self.current_channel = 1

    def next_channel(self):
        print('Going to next channel...')
        self.set_channel(self.current_channel + 1)

    def prev_channel(self):
        print('Going to previous channel...')
        self.set_channel(self.current_channel - 1)

    def set_channel(self, channel):
        self.tv.tune_channel(channel)
        self.current_channel = channel


class SonyTV(TV):
    def on(self):
        print('Turning Sony TV on')

    def off(self):
        print('Turning Sony TV off')

    def tune_channel(self, channel: int):
        print('Sony: Now in Channel {}'.format(channel))


class TclTV(TV):
    def on(self):
        print('Turning TCL TV on')

    def off(self):
        print('Turning TCL TV off')

    def tune_channel(self, channel: int):
        print('TCL: Setting Now in Channel {}'.format(channel))
