import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_positive(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtract_positive(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiply_positive(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_by_negative(self):
        self.assertEqual(self.calc.multiply(3, -2), -6)

    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    def test_divide_by_negative(self):
        self.assertEqual(self.calc.divide(6, -2), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_modulo_positive(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)

    def test_modulo_negative(self):
        self.assertEqual(self.calc.modulo(-5, 2), -1)

    def test_modulo_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(5, 0)

if __name__ == '__main__':
    unittest.main()
