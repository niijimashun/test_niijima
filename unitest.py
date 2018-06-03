#!/usr/bin/env python

import unittest
from plus import plus

class TestPlus(unittest.TestCase):
    def test_init(self):
        self.assertEqual(plus(1,2),3,"void int が間違ってます")

    def test_float(self):
        self.assertTrue(3.299999 < plus(1.1,2.2) < 3.300001, "error on float")



unittest.main()

