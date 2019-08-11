from vacation_planner import AbstractBuilder


def construct_planner():
    builder = AbstractBuilder()
    builder.build_day('2019-09-11')
    builder.add_hotel('Hilton Beijing')
    builder.add_restaurant('UTown')
    builder.add_special_event('Visiting a friend')
    builder.add_ticket('Forbidden city')

    builder.build_day('2019-09-12')
    builder.add_hotel('Hilton Beijing')
    builder.add_restaurant('UTown')

    # FIXME: should display multiple tickets if there are so
    builder.build_day('2019-09-13')
    builder.add_ticket('Forbidden city')
    builder.add_ticket('798 Picasso')

    print(builder.get_plans())
    builder.print_vacation_plans()


construct_planner()
