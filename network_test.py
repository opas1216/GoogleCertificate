#!/usr/bin/env python3

import unittest
import requests
from network import check_localhost
from network import check_connectivity

class TestCheckNetwork(unittest.TestCase):
    def test_localhost(self):
        # testcase = socket.gethostbyname('localhost')
        # expected = True
        # self.assertEqual(check_localhost(), expected)
        self.assertTrue(check_localhost())

    def test_connectivity(self):
        testcase = requests.get("http://www.google.com").status_code
        # expected = True
        # self.assertEqual(check_connectivity(), expected)
        self.assertTrue(check_connectivity())



unittest.main()
