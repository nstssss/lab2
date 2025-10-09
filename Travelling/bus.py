from Travelling.transport import Transport
"""КЛАСС АВТОБУСНОГО МАРШРУТА"""
class Bus(Transport):
    """констуктор класса"""
    def __init__(self, distance, passengers, ticket_price):
        self._distance = distance
        self._passengers = passengers
        self._ticket_price = ticket_price
        self.average_speed = 50 #средняя скорость автобуса
    @property
    def distance(self):
        return self._distance
    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def passengers(self):
        return self._passengers
    @passengers.setter
    def passengers(self, value):
        self._passengers = value
    @property
    def ticket_price(self):
        return self._ticket_price
    @ticket_price.setter
    def ticket_price(self, value):
        self._ticket_price = value

    """расчет стоимости маршрута"""
    def calculate_cost(self):
        return self.passengers * self.ticket_price
    """расчет времени поездки"""
    def calculate_time(self):
        return self.distance / self.average_speed
    """расчет пассажиропотока"""
    def calculate_passenger_flow(self):
        return self.passengers * self.distance

    def __str__(self):
        return (f"Автобус. Длина маршрута: {self.distance()},"
                f" количество пассажиров {self.passengers()},"
                f" стоимость билета {self.ticket_price()}")