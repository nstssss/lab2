import pytest
from Travelling.bus import Bus
from Travelling.train import Train
from Travelling.plane import Plane

#тесты для класса bus
def test_init_bus():
    bus = Bus(100, 50, 250)

    assert bus.distance == 100
    assert bus.passengers == 50
    assert bus.ticket_price == 250
    assert bus.average_speed == 50

def test_init_bus2():
    bus = Bus(0, 0, 0)
    assert bus.calculate_cost() == 0
    assert bus.calculate_time() == 0
    assert bus.calculate_passenger_flow() == 0


def test_calculate_cost_bus():
    bus = Bus(200, 40, 300)
    expected_cost = 40 * 300
    assert bus.calculate_cost() == expected_cost

def test_calculate_time_bus():
    bus = Bus(150, 30, 20.0)
    expected_time = 150 / 50
    assert bus.calculate_time() == expected_time
    assert bus.calculate_time() == 3.0

def test_calculate_passenger_flow_bus():
    bus = Bus(100, 25, 15.5)
    expected_flow = 25 * 100
    assert bus.calculate_passenger_flow() == expected_flow
    assert bus.calculate_passenger_flow() == 2500

def test_property_setters_bus():
        bus = Bus(100, 50, 25.0)
        bus.distance = 200
        bus.passengers = 60
        bus.ticket_price = 30.0

        assert bus.distance == 200
        assert bus.passengers == 60
        assert bus.ticket_price == 30.0

#тесты для класса Train
def test_train_init_train():
    train = Train(500, 300, 150.0)

    assert train.distance == 500
    assert train.passengers == 300
    assert train.ticket_price == 150.0
    assert train.average_speed == 100

def test_calculate_cost_train():
    train = Train(400, 250, 120.0)
    expected_cost = 250 * 120.0

    assert train.calculate_cost() == expected_cost
    assert train.calculate_cost() == 30000.0

def test_calculate_time_train():
    train = Train(300, 200, 100.0)
    expected_time = 300 / 100

    assert train.calculate_time() == expected_time
    assert train.calculate_time() == 3.0

def test_calculate_passenger_flow_train():
    train = Train(200, 150, 80.0)
    expected_flow = 150 * 200

    assert train.calculate_passenger_flow() == expected_flow
    assert train.calculate_passenger_flow() == 30000

def test_property_setters_train():
    train = Train(350, 180, 90.0)
    train.distance = 450
    train.passengers = 220
    train.ticket_price = 110.0

    assert train.distance == 450
    assert train.passengers == 220
    assert train.ticket_price == 110.0

#тесты для класса Plane
def test_plane_initialization():
    plane = Plane(2000, 180, 5000.0)

    assert plane.distance == 2000
    assert plane.passengers == 180
    assert plane.ticket_price == 5000.0
    assert plane.average_speed == 800

def test_calculate_cost():
    plane = Plane(1500, 150, 4000.0)
    expected_cost = 150 * 4000.0

    assert plane.calculate_cost() == expected_cost
    assert plane.calculate_cost() == 600000.0

def test_calculate_time():
    plane = Plane(2400, 200, 3500.0)
    expected_time = 2400 / 800

    assert plane.calculate_time() == expected_time
    assert plane.calculate_time() == 3.0

def test_calculate_passenger_flow():
    plane = Plane(1000, 120, 2500.0)
    expected_flow = 120 * 1000

    assert plane.calculate_passenger_flow() == expected_flow
    assert plane.calculate_passenger_flow() == 120000
    assert isinstance(plane.calculate_passenger_flow(), (int, float))

def test_property_setters():
    plane = Plane(3000, 250, 6000.0)

    plane.distance = 4000
    plane.passengers = 300
    plane.ticket_price = 5500.0

    assert plane.distance == 4000
    assert plane.passengers == 300
    assert plane.ticket_price == 5500.0