"""
In this weather station, we have an software that generate weather stats (WeatherData) and we need to build two boards
to display the data generated from WeatherData.

To do this, we create a one-to-many object relationship, in which once the WeatherData generates new data, all the boards
receive the data automatically. We could think of this relation as Subject and Subscriber which WeatherData is the subject
and displays the subscribers.

Design principle(s):
    Loose coupling between interative objects is what we should pursuit.

"""
from observer_pattern.weather_data_subject import WeatherData
from observer_pattern.displays import CurrentConditionsDisplay, StatisticsDisplay

subject = WeatherData()
current_display = CurrentConditionsDisplay(subject)
stats_display = StatisticsDisplay(subject)
print('----- CurrentConditionDisplay -----')
current_display.display()
print('----- StatisticsDisplay -----')
stats_display.display()
print('----- WeatherData got new stats -----')
subject.measurement_changed()
print('----- CurrentConditionDisplay -----')
current_display.display()
print('----- StatisticsDisplay -----')
stats_display.display()
print('----- WeatherData sent new data to displays -----')
subject.notify_observers()
print('----- CurrentConditionDisplay -----')
current_display.display()
print('----- StatisticsDisplay -----')
stats_display.display()