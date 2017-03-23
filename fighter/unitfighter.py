import random
import unittest
from fighter.fighterjet import *
from unittest.mock import MagicMock, Mock

class SimpleTest(unittest.TestCase):

    #This is called before every test
    def setUp(self):

        self.radar_mock = MagicMock(return_value=None)
        self.radar = RadarSystem()
        self.radar.get_closest = self.radar_mock

        self.weapons_system_mock = Mock()

        self.fighter = FighterJet(self.radar, self.weapons_system_mock)

    #what were my test cases?

    def test_no_target_no_fire(self):
        self.radar_mock.return_value = None

        self.fighter.reassess()

        self.weapons_system_mock.fire.assert_not_called()


    def test_friendly_fire_isnt_friendly(self):
        self.radar_mock.return_value = RadarSignature(distance=10, friendly=True, id="Maverick", type="F16")

        self.fighter.reassess()

        self.weapons_system_mock.fire.assert_not_called()


    def test_fire_on_enemy(self):
        viper = RadarSignature(distance=10, friendly=False, id="Viper", type="F16")

        self.radar_mock.return_value = viper

        self.fighter.reassess()

        self.weapons_system_mock.fire.assert_called()
        self.weapons_system_mock.fire.assert_called_with(viper)


if __name__ == '__main__':
    unittest.main()
