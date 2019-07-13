from observer_pattern.interfaces import ObserverInterface, DisplayElementInterface, SubjectInterface


class CurrentConditionsDisplay(ObserverInterface, DisplayElementInterface):
    # display current stats from WeatherData
    def __init__(self, subject: callable(SubjectInterface)) -> None:
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.subject = subject
        self.subject.register_observer(self)

    def update(self, temperature, humidity, pressure) -> None:
        self.humidity = humidity
        self.temperature = temperature
        self.pressure = pressure

    def display(self) -> tuple:
        print(f"Temperature: {self.temperature}. Humidity: {self.humidity}. Pressure: {self.pressure}")
        return self.temperature, self.humidity, self.pressure


class StatisticsDisplay(ObserverInterface, DisplayElementInterface):
    # display highest, average and lowest stats
    def __init__(self, subject: callable):
        self.highest_temp = float('-inf')
        self.lowest_temp = float('inf')
        self.average_temp = 0
        self.highest_humidity = float('-inf')
        self.lowest_humidity = float('inf')
        self.average_humidity = 0
        self.highest_pressure = float('-inf')
        self.lowest_pressure = float('inf')
        self.average_pressure = 0
        self.count = 0
        self.subject = subject
        self.subject.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.count += 1
        print(1111111)
        print(temperature, self.highest_temp)
        self.highest_temp = max(temperature, self.highest_temp)
        self.lowest_temp = min(temperature, self.lowest_temp)
        self.average_temp = (self.average_temp + temperature) / self.count
        self.highest_humidity = max(humidity, self.highest_humidity)
        self.lowest_humidity = min(humidity, self.lowest_humidity)
        self.average_humidity = (self.average_humidity + humidity) / self.count
        self.highest_pressure = max(pressure, self.highest_pressure)
        self.lowest_pressure = min(pressure, self.lowest_pressure)
        self.average_pressure = (self.average_pressure + pressure) / self.count

    def display(self):
        print(f"""Temperature High: {self.highest_temp}. 
        Humidity High: {self.highest_humidity}. 
        Pressure High: {self.highest_pressure}\n 
        Temperature Low: {self.lowest_temp}. 
        Humidity Low: {self.lowest_humidity}. 
        Pressure Low: {self.lowest_pressure}\n 
        Temperature Avg: {self.average_temp}. 
        Humidity Avg: {self.average_humidity}. 
        Pressure Avg: {self.average_pressure}""")


class ForecastDisplay(ObserverInterface, DisplayElementInterface):
    # display weather forecast according to pressure
    def update(self, temperature, humidity, pressure):
        pass

    def display(self):
        pass
