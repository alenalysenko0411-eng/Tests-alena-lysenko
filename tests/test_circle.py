"""Unit-тесты модуля circle.py (круг).

Ожидаемые значения взяты из формул в docs/README.md:
площадь S = pi * R^2, периметр (длина окружности) P = 2 * pi * R.

Пример запуска:
    python -m unittest tests.test_circle -v
"""
import math
import unittest

import circle


class CircleAreaTestCase(unittest.TestCase):
    """Тесты функции circle.area(r)."""

    def test_area_unit_radius(self):
        """Круг радиуса 1: площадь равна pi.

        Пример: circle.area(1) -> 3.14159...
        """
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_zero_radius(self):
        """Круг нулевого радиуса: площадь 0.

        Пример: circle.area(0) -> 0
        """
        self.assertEqual(circle.area(0), 0)

    def test_area_fractional_radius(self):
        """Дробный радиус 2.5: площадь 6.25 * pi = 19.63495...

        Пример: circle.area(2.5) -> 19.63495...
        """
        self.assertAlmostEqual(circle.area(2.5), 19.634954084936208)

    def test_area_big_radius(self):
        """Большой радиус 1000: площадь 1 000 000 * pi.

        Пример: circle.area(1000) -> 3141592.65...
        """
        self.assertAlmostEqual(circle.area(1000), 3141592.653589793, places=5)

    def test_area_small_radius(self):
        """Маленький радиус 0.1: площадь 0.01 * pi = 0.0314159...

        Пример: circle.area(0.1) -> 0.0314159...
        """
        self.assertAlmostEqual(circle.area(0.1), 0.031415926535897934)

    def test_area_string_radius(self):
        """Строка вместо числа должна вызывать TypeError.

        Пример: circle.area('5') -> TypeError
        """
        with self.assertRaises(TypeError):
            circle.area('5')


class CirclePerimeterTestCase(unittest.TestCase):
    """Тесты функции circle.perimeter(r)."""

    def test_perimeter_unit_radius(self):
        """Радиус 1: длина окружности 2 * pi.

        Пример: circle.perimeter(1) -> 6.28318...
        """
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)

    def test_perimeter_zero_radius(self):
        """Радиус 0: длина окружности 0.

        Пример: circle.perimeter(0) -> 0
        """
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_fractional_radius(self):
        """Радиус 2.5: длина окружности 5 * pi = 15.70796...

        Пример: circle.perimeter(2.5) -> 15.70796...
        """
        self.assertAlmostEqual(circle.perimeter(2.5), 15.707963267948966)


if __name__ == '__main__':
    unittest.main()
