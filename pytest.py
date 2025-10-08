from Travelling.bus import Bus

class test_Bus:

    def init_bus(self):
        bus = Bus(100, 50, 250)

        assert bus.distance == 100
        assert bus.passengers == 50
        assert bus.ticket_price == 250
        assert bus.average_speed == 50

    def test_calculate_cost(self):
        """Тест расчета стоимости маршрута"""
        bus = Bus(200, 40, 30.0)
        expected_cost = 40 * 30.0  # passengers * ticket_price

        assert bus.calculate_cost() == expected_cost
        assert isinstance(bus.calculate_cost(), (int, float))