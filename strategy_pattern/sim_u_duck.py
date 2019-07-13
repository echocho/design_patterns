"""
SimUDuck, a program simulating different types of duck, including their appearance and behavior.

Design principles:
    Understand and figure out what may be changed in the future, separate them with those won't need to be changed.
    Don't mixed them together.

    Code for interface, not for implementation.

    Use more composition, less inheritance.

Inheritance is not useful here because even though all ducks can swim and have appearance, ducks fly in different ways --
some fly, some don't, and make different sounds -- some squeak, some quack and some are just mute.
If we use inheritance, it means some subclass have to inherit some thing they are not or use.

Furthermore, if we need to change the implementation of the duck, say, we want a super duck to fly with a rocket, we have
to rewrite the implementation, override the inherited fly() method from parent class, or provide a totally new method for
user to call. However, if we use composition, we can changed the implementation and the users won't even notice.
For example, we create two interfaces, FlyBehavior and QuackBehavior, and build specific behaviors extending those two,
e.g. FlyNoWay, FlyWithWings, MuteQuack, Squeak. And then in the specific duck object (class, e.g. MallardDuck) we composite
the abstract method fly() with specific fly behavior. Same logic applies to quack().
"""

from intro.duck_behaviors import FlyNoWay, FlyWithWings, Quack, MuteQuack
from intro.duck_base import DuckBaseType


class MallardDuck(DuckBaseType):
    def __init__(self):
        self.name = "A real mallard duck"

    def fly(self):
        return FlyWithWings().fly()

    def quack(self):
        return Quack().quack()


class RubberDuck(DuckBaseType):
    def __init__(self):
        self.name = "A real robber duck"

    def fly(self):
        return FlyNoWay().fly()

    def quack(self):
        return MuteQuack().quack()

