import unittest

def area(a, b): 
    '''
    Функция получает на вход два числа a и b - длины сторон прямоугольника.
    Возвращает число - площадь прямоугольника со сторонами a и b.
    '''
    return a * b 

def perimeter(a, b): 
    '''
    Функция получает на вход два числа a и b - длины сторон прямоугольника.
    Возвращает число - периметр прямоугольника со сторонами a и b.
    '''
    return (a + b) * 2
def diagonal(a, b):
    '''
    Функция получает на вход два числа a и b - длины сторон прямоугольника.
    Возвращает число - диоганаль прямоугольника со сторонами a и b.
    '''
    return (a**2 + b**2)**0.5
    

class RectangleTestCase(unittest.TestCase):
    def test_null_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)
    def test_null_perimeter(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)
    def test_area(self):
        res = area(2, 30)
        self.assertEqual(res, 60)
    def test_perimeter(self):
        res = perimeter(2, 30)
        self.assertEqual(res, 64)
    def test_dioganal(self):
        res = diagonal(3, 4)
        self.assertEqual(res, 5)