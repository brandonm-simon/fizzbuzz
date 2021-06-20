import unittest
from fizzbuzz.helpers import (
    check_if_valid, get_error_code,
    transform1, transform2, transform3
)

class TestCheckIfValid(unittest.TestCase):

    def test_valid(self):
        row = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.assertTrue(check_if_valid(row), True)

    def test_invalid(self):
        row = [1,2,'A',4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        self.assertFalse(check_if_valid(row), True)


class TestGetErrorCode(unittest.TestCase):

    def test_column_error(self):
        row = [1,2,'A',4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.assertEqual(get_error_code(row), 'non_integer')

    def test_length_error(self):
        row = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        self.assertEqual(get_error_code(row), 'column_error')


class TestTransform1(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(transform1(3), 'fizz')

    def test_buzz(self):
        self.assertEqual(transform1(5), 'buzz')

    def test_fizzbuzz(self):
        self.assertEqual(transform1(15), 'fizzbuzz')

    def test_none(self):
        self.assertEqual(transform1(1), 1)


class TestTransform2(unittest.TestCase):

    def test_lucky(self):
        self.assertEqual(transform2(13), 'lucky')

    def test_none(self):
        self.assertEqual(transform2(1), 1)


class TestTransform3(unittest.TestCase):

    def test_report(self):
        input = [1, 2, 'lucky', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz',
              'lucky', 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz']
        output = {'fizz': 4, 'buzz': 3, 'fizzbuzz': 1, 'lucky': 2, 'integer': 10}
        self.assertEqual(transform3(input), output)
        self.assertIsInstance(transform3(input), dict)

if __name__ == '__main__':
    unittest.main()