"""
Requirements:
    set alarm at 7am in trash days
    set alarm at 10am in weekends
    set alarm at 8am in weekdays
    different coffee for different day in the week
    start coffee machine when the alarm snooze button is pressed
    turn on sprinkler after coffee machine starts
    no coffee in weekends, start sprinkler when the alarm snooze button is pressed
    turn off sprinkler when bath tub is ready
"""
from mediator_pattern.appliances import Alarm, BathTub, Calendar, CoffeePot, Sprinkler


class Mediator(object):
    alarm = Alarm()
    calendar = Calendar()
    coffee_machine = CoffeePot()
    sprinkler = Sprinkler()
    bath_tub = BathTub()
    coffee_list = None
    today = None

    def set_alarm_for_weekdays(self, time=8):
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            self.alarm.set_alarm(time, day)

    def set_alarm_for_weekends(self, time=10):
        for day in ['Saturday', 'Sunday']:
            self.alarm.set_alarm(time, day)

    def set_alarm_for_trash_days(self, time=7):
        trash_day = 'Friday'
        self.alarm.set_alarm(time, trash_day)

    def set_coffee_type_for_different_days(self, coffee_days=None):
        if coffee_days:
            self.coffee_list = coffee_days
        else:
            self.coffee_list = {'Monday': 'Espresso', 'Tuesday': 'Latte', 'Wednesday': 'Americano',
                                'Thursday': 'Mocha', 'Friday': 'Cappuccino'}

    def schedule(self):
        sprinkler_off = False
        self.today = self.calendar.check_day_of_week()
        print(f'Today is {self.today}')
        self.alarm.ring()
        if self.alarm.snoozed:
            if self._is_weekday(self.today):
                self.coffee_machine.make_coffee(self.coffee_list.get(self.today))
            self.sprinkler.turn_on()
            while not sprinkler_off:
                if self.bath_tub.is_ready():
                    self.sprinkler.turn_off()
                    sprinkler_off = True
        return

    @staticmethod
    def _is_weekday(day):
        return True if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] else False


if __name__ == '__main__':
    mediator = Mediator()
    # mediator.set_alarm_for_weekdays()
    # mediator.set_alarm_for_trash_days()
    # mediator.set_alarm_for_weekends()
    mediator.set_coffee_type_for_different_days()
    mediator.schedule()
