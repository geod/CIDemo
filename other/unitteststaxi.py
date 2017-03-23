import random
import unittest

from taximeter import TaxiMeter


class SimpleTest(unittest.TestCase):

    def test_pass(self):
        tm = TaxiMeter()

        self.assertEqual(tm.calculate_fare(1.4, 20), 7.5)

        #self.assertEqual(tm.calculate_fare(51, 60), 15.25)




