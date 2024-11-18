import unittest

def area(a, h):
    '''
    Функция получает на вход два числа a и h - длина стороны треугольника и 
    длина высоты, проведенной к этой стороне.
    Возвращает число - площадь треугольника со стороной треугольника a 
    и высотой, проведенной к этой стороне, h.
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Функция получает на вход три числа **a**, **b** и **c** - длины сторон треугольника.
    Возвращает число - периметр треугольника со сторонами **a**, **b** и **c**.
    '''
    return a + b + c 

class RectangleTestCase(unittest.TestCase):
    def test_null_area(self):
        res = area(1000, 0)
        self.assertEqual(res, 0)
    def test_null_perimeter(self):
        res = perimeter(0,0,0)
        self.assertEqual(res, 0)
    def test_area(self):
        res = area(30,4)
        self.assertEqual(res, 60)
    def test_perimeter(self):
        res = perimeter(30, 30 , 30)
        self.assertEqual(res, 90)