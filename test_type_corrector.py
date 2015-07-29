import unittest

from typecorrector import type_corrector


######################################################
# Functions for testing the type corrector decorator #
######################################################

@type_corrector(int, int)
def add(a, b=0):
    """Adds two numbers"""
    return a+b


@type_corrector(int)
def mult(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

@type_corrector(int)
def kw_mult(**kwargs):
    first = kwargs.get('first')
    second = kwargs.get('second')
    third = kwargs.get('third')
    
    return first * second * third

######################################################
# End test functions                                 #
######################################################


class TypeCorrectorTest(unittest.TestCase):
    def test_add1(self):
        self.assertEqual(add(1, 2), 3)

    def test_add2(self):
        self.assertEqual(add('1', 2), 3)

    def test_add3(self):
        self.assertEqual(add('1', '2'), 3)
    
    def test_add4(self):
        self.assertEqual(add(1, b=2), 3)

    def test_add5(self):
        self.assertEqual(add('1', b=2), 3)

    def test_add6(self):
        self.assertEqual(add('1', b='2'), 3)

    def test_mult1(self):
        self.assertEqual(mult(2, 3, 4), 24)
    
    def test_mult2(self):
        self.assertEqual(mult('2', 3, 4), 24)  
    
    def test_mult3(self):
        self.assertEqual(mult('2', '3', 4), 24)  
    
    def test_mult4(self):
        self.assertEqual(mult('2', '3', '4'), 24)

    def test_kw_mult1(self):
        return self.assertEqual(kw_mult(first=2, second=3, third=4), 24)
    
    def test_kw_mult2(self):
        return self.assertEqual(kw_mult(first='2', second=3, third=4), 24)
    
    def test_kw_mult3(self):
        return self.assertEqual(kw_mult(first='2', second='3', third=4), 24)
    
    def test_kw_mult4(self):
        return self.assertEqual(kw_mult(first='2', second='3', third='4'), 24)
    

if __name__ == '__main__':
    unittest.main()
    
