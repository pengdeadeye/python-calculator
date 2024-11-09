import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)



    def test_add1(self):
        self.assertEqual(self.calc.add(3, 5), 8)
    def test_add2(self):
        self.assertEqual(self.calc.add(4, -2), 2) 
        

        
    def test_substract1(self):
        self.assertEqual(self.calc.substract(4, -2), 6) 
    def test_substract2(self):
        self.assertEqual(self.calc.substract(5, 3),2)



    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(5, 3),15)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(1, -5), -5)



    def test_divide1(self):
        self.assertEqual(self.calc.divide(6, 3),2)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(-6, 3),-2)


    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(5, 3),2)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(5, 3),2)







    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()