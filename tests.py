import unittest
from calculadora import soma
from calculadora import sub
from calculadora import mult
from calculadora import div

class TestCalcula(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(1,1), 2)
        self.assertEqual(soma(-1,5), 4)
        self.assertEqual(soma(0,-5), -5)
    def test_sub(self):
        self.assertEqual(sub(1,1), 0)
        self.assertEqual(sub(-1,5), -6)
        self.assertEqual(sub(0,-5), 5)
    def test_mult(self):
        self.assertEqual(mult(1,1), 1)
        self.assertEqual(mult(-1,5), -5)
        self.assertEqual(mult(0,-5), 0)
    def test_div(self):
        self.assertEqual(div(1,1), 1)
        self.assertEqual(div(-1,5), -0.2)
        self.assertEqual(div(0,-5), 0)
        self.assertEqual(div(10,0), "erro")


if __name__ == '__main__':
    unittest.main()