import unittest
from fibonacci import fibonacci, is_fibonacci


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_values(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)

    def test_is_fibonacci(self):
        for n in:
            self.assertTrue(is_fibonacci(n))
        for n in [-1, 4, 6, 7, 10]:
            self.assertFalse(is_fibonacci(n))


if __name__ == "__main__":
    unittest.main()
