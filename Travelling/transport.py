import abc
from abc import ABC, abstractmethod
"""абстрактный класс транспорта"""
class Transport(ABC):

    @abc.abstractmethod
    def calculate_cost(self):
        pass

    @abc.abstractmethod
    def calculate_time(self):
        pass

    @abc.abstractmethod
    def calculate_passenger_flow(self):
        pass