import random
from typing import Optional

from observer_pattern.interfaces import SubjectInterface


class WeatherData(SubjectInterface):
    def __init__(self):
        super().__init__()
        self.humidity: Optional[float] = None
        self.temperature: Optional[float] = None
        self.pressure: Optional[float] = None

    @staticmethod
    def get_temperature() -> float:
        return random.uniform(-30, 45)

    @staticmethod
    def get_humidity() -> float:
        return random.uniform(0, 100)

    @staticmethod
    def get_pressure() -> float:
        return random.uniform(-50, 500)

    def measurement_changed(self) -> None:
        new_temperature = self.get_temperature()
        new_humidity = self.get_humidity()
        new_pressure = self.get_pressure()
        if new_temperature != self.temperature or new_humidity != self.humidity or new_pressure != self.pressure:
            self.temperature = new_temperature
            self.humidity = new_temperature
            self.pressure = new_pressure
        self.notify_observers()
        print(f"""Updates from WeatherData.\n
        New temperature is {new_temperature}, new humidity is {new_humidity}, and new pressure is {new_pressure}""")

    def notify_observers(self):
        for observer in self.observers:
            observer.update(temperature=self.temperature, humidity=self.humidity, pressure=self.pressure)
