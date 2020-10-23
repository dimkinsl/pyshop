#! Python3
# Тест-кейс для функции is_even

import unittest
from is_even import is_even

class TestIsEven(unittest.TestCase):

    def test_is_even(self):
        self.assertEqual(is_even(4), True, 'True is even')

    def test_is_odd(self):
        self.assertEqual(is_even(5), False, 'False is odd')

    def test_is_not_number(self):
        self.assertEqual(is_even('5'), False, 'TypeError: string formatting')

    def test_zero(self):
        self.assertEqual(is_even(), True, 'Missing 1 required positional argument')



if __name__ == '__main__':
    unittest.main()