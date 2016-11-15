import random
from wraparoundcounter import WrapAroundCounter

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class SimpleTest(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_skipped(self):
        self.fail("shouldn't happen")


    def test_pass(self):
        wac = WrapAroundCounter(10)

        self.assertEqual(wac.increment(1), 2)
        self.assertEqual(wac.increment(9), 10)
        self.assertEqual(wac.increment(10), 1)
