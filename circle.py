import math
import unittest

def area(r):
    '''
    Функция получает на вход число r - длину радиуса окружности.
    Возвращает число - площадь окружности с радиусом r.
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Функция получает на вход число r - длину радиуса окружности.
    Возвращает число - периметр окружности с радиусом r.
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_null_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_null_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_area(self):
        res = area(2)
        self.assertEqual(res, 12.566370614359172)
    def test_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 12.566370614359172)
        