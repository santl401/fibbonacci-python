import unittest
from fibonacci import fibonacci, is_fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_values(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)

    def test_is_fibonacci(self):
        valid_nums = (0, 1, 2, 3, 5, 8, 13, 21, 34, 55)
        invalid_nums = (-1, 4, 6, 7, 10)
        for n in valid_nums:
            self.assertTrue(is_fibonacci(n))
        for n in invalid_nums:
            self.assertFalse(is_fibonacci(n))


if __name__ == "__main__":
    unittest.main()
