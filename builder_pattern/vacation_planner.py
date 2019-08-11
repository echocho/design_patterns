from abc import ABCMeta, abstractmethod


class VacationBuilder(object):
    vacation = None
    activity_date = None
    plans = []
    current_day = None

    def build_day(self, date: str):
        one_day_plan = OneDayPlan(date)
        self.plans.append(one_day_plan)
        self.activity_date = date
        self.current_day = self.plans[-1]

    def add_hotel(self, name: str):
        self.current_day.hotel['name'] = name

    def add_restaurant(self, name: str):
        self.current_day.restaurant['name'] = name

    def add_special_event(self, name: str):
        self.current_day.special_event['name'] = name

    def add_ticket(self, name: str):
        self.current_day.ticket['name'] = name

    def get_plans(self):
        return self.plans

    def print_vacation_plans(self):
        for plan in self.plans:
            print(f"***********{plan.activity_date}***********")
            print(f"Hotel: {plan.hotel['name']}")
            print(f"Restaurant: {plan.restaurant['name']}")
            print(f"special_event: {plan.special_event['name']}")
            print(f"ticket: {plan.ticket['name']}")
            print("\n")


class AbstractBuilder(object):

    builder = VacationBuilder()

    def build_day(self, date: str):
        self.builder.build_day(date)

    def add_hotel(self, name: str):
        self.builder.add_hotel(name)

    def add_restaurant(self, name: str):
        self.builder.add_restaurant(name)

    def add_special_event(self, name: str):
        self.builder.add_special_event(name)

    def add_ticket(self, name: str):
        self.builder.add_ticket(name)

    def get_plans(self):
        self.builder.get_plans()

    def print_vacation_plans(self):
        self.builder.print_vacation_plans()


class OneDayPlan(object):
    def __init__(self, date: str):
        self.activity_date = date
        self.hotel = {"name": None, "date": self.activity_date}
        self.restaurant = {"name": None, "date": self.activity_date}
        self.special_event = {"name": None, "date": self.activity_date}
        self.ticket = {"name": None, "date": self.activity_date}
