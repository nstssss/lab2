class Plane():
    def __init__(self, distance, passengers, ticket_price):
        self.distance = distance
        self.passengers = passengers
        self.ticket_price = ticket_price
        self.average_speed = 800
"""расчет стоимости маршрута"""
def calculate_cost(self):
    return self.passengers * self.ticket_price
"""расчет времени поездки"""
def calculate_time(self):
    return self.distance / self.average_speed
"""расчет пассажиропотока"""
def calculate_passenger_flow(self):
    return self.passengers * self.distance