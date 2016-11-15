import random
from wraparoundcounter import WrapAroundCounter

import json
import requests

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class SimpleIntegrationTest(unittest.TestCase):

    def test_pass(self):
        url = 'http://localhost:5000/counter/10'
        res = requests.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.text, '{\n  \"incremented\": 1\n}')


    def test_malformed(self):
        url = 'http://localhost:5000/counter/foobar'
        res = requests.get(url)
        self.assertEqual(res.status_code, 500)

