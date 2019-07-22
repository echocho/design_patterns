"""
Facade-Pattern provides a simplified interface to a larger group of interfaces (code), which
is usually more complex or structural underlying, such as a class library.
This pattern defines a high level interface, the underlying code easier to use.

Difference between facade pattern and adapter pattern: the former to simplifies interfaces
and the later convert one interface to anther interface

Design principle(s):
Law of Demeter/ principle of least knowledge
    1. each unit should have limited knowledge of other units: only units "closely" related to the
    current unit.
    2. each unit should only talk to its friends; don't talk to strangers
    3. only talk to your immediate friends

"""
from adapter_pattern.home_theater_underlying import (PopcornPopper, TheaterLights, Screen, Projector,
                                                     Amplifier, DVDPlayer)


class HomeTheaterFacade(object):
    popper = PopcornPopper()
    lights = TheaterLights()
    screen = Screen()
    projector = Projector()
    amp = Amplifier()
    player = DVDPlayer()

    def watch_movie(self):
        self.popper.on()
        self.popper.pop()

        self.lights.on()
        self.lights.dim()

        self.screen.down()

        self.projector.on()
        self.projector.tv_mode('DVD')
        self.projector.wide_screen_mode()

        self.amp.on()
        self.amp.set_dvd()
        self.amp.set_surround_sound()
        self.amp.set_volume(5)

        self.player.on()
        self.player.play("Love, Pray, Eat")

    # Similar logic for finishing movie/ turning off everything ...


t = HomeTheaterFacade()
t.watch_movie()


