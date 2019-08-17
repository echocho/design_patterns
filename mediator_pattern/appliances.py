import random


class Alarm(object):
    snoozed = None

    @staticmethod
    def set_alarm(time, day):
        print(f'Set alarm at {time} on {day}')

    def ring(self):
        option = input('Time to get up! Or enter 1 to snooze: ')
        if option == '1':
            self.snoozed = True


class CoffeePot(object):
    @staticmethod
    def make_coffee(coffee):
        print(f'Make {coffee} today')


class Calendar(object):
    @staticmethod
    def check_day_of_week():
        days = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
        return random.choice(days)


class Sprinkler(object):
    @staticmethod
    def turn_off():
        print('Turn off sprinkler')

    @staticmethod
    def turn_on():
        print('Turn on sprinkler')


class BathTub(object):
    @staticmethod
    def is_ready():
        random_val = random.choice([i for i in range(5)])
        return random_val == 1
