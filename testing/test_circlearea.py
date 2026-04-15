import unittest
from testing.service import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(2), pi * 4)

    def test_value(self):
        self.assertRaises(ValueError, circle_area, -1)
        self.assertRaises(ValueError, circle_area, -4.5)

    def test_types(self):
        self.assertRaises(TypeError, circle_area, [1, 2])
        self.assertRaises(TypeError, circle_area, "hi")
        self.assertRaises(TypeError, circle_area, (1,))
