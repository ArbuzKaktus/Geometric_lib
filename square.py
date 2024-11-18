import unittest

def area(a):
    '''
    Функция получает на вход число a - длина стороны квадрата.
    Возвращает число - площадь квадрата со стороной a.
    '''
    return a * a


def perimeter(a):
    '''
    Функция получает на вход число a - длина стороны квадрата.
    Возвращает число - периметр квадрата со стороной a.
    '''
    return 4 * a

def diagonal(a):
    '''
    Функция получает на вход число a - длина стороны квадрата.
    Возвращает число - диоганаль квадрата со стороной a.
    '''
    return a * (2 ** 0.5)

class RectangleTestCase(unittest.TestCase):
    def test_null_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_null_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_area(self):
        res = area(30)
        self.assertEqual(res, 900)
    def test_perimeter(self):
        res = perimeter(30)
        self.assertEqual(res, 120)
    def test_diagonal(self):
        res = diagonal(4)
        self.assertEqual(res, 4 * (2 ** 0.5))