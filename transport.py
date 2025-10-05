import abc
from abc import ABC, abstractmethod
"""абстрактный класс транспорта"""
class Transport(ABC):
    # def __init__(self, distance, passengers, ticket_price):
    #     self.distance = distance
    #     self.passengers = passengers
    #     self.ticket_price = ticket_price
    #     self.average_speed = self.get_speed()
    # @abstractmethod
    # def get_speed(self):
    #     pass

    @abc.abstractmethod
    def calculate_cost(self):
        pass

    @abc.abstractmethod
    def calculate_time(self):
        pass

    @abc.abstractmethod
    def calculate_passenger_flow(self):
        pass