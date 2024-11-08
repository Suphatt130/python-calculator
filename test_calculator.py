import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add1(self):
        self.assertEqual(self.calc.add(10, 5), 15)
    
    def test_add2(self):
        self.assertEqual(self.calc.add(9, 0), 9)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(0, 7), -7)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    def test_mul1(self):
        self.assertEqual(self.calc.multiply(9, 9), 81)

    def test_mul2(self):
        self.assertEqual(self.calc.multiply(3, 3), 9)   

    def test_divide1(self):
        self.assertEqual(self.calc.divide(2, 2), 1)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(25, 5), 5)

    def test_module1(self):
        self.assertEqual(self.calc.modulo(10, 2), 0)

    def test_module2(self):
        self.assertEqual(self.calc.modulo(100, 5), 0)


if __name__ == '__main__':
    unittest.main()