import abc
from abc import ABC, abstractmethod
"""абстрактный класс транспорта"""
class Transport(ABC):
#абстрактный метод расчета стоимости маршрута
    @abc.abstractmethod
    def calculate_cost(self):
        pass
#абстрактный метод расчета времени поездки
    @abc.abstractmethod
    def calculate_time(self):
        pass
#абстрактный метод расчета пассажиропотока
    @abc.abstractmethod
    def calculate_passenger_flow(self):
        pass